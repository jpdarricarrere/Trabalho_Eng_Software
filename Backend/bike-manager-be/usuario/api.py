from fastapi import APIRouter 

from .Sessao import Sessao
from .integracao.DTOLoginRequest import DTOLoginRequest
from .persistencia.InMemoryRepositorioUsuario import InMemoryRepositorioUsuario as RepositorioUsuario


router = APIRouter(
    prefix = '/usuarios'
)

sessoes = Sessao()

@router.get("/")
def get_usuarios():
    encontrados = RepositorioUsuario.get_all()
    return [u.dto() for u in encontrados]

@router.post('/login')
def login(dados: DTOLoginRequest) -> dict:
    if dados.email == '' or dados.senha == '':
        return dict()

    return sessoes.login(dados.email, dados.senha)

@router.get('/logout')
def logout(email: str = '', token: str = ''):
    if email == '' or token == '':
        return 

    sessoes.logout(email, token)

@router.get('/todas_sessoes')  # PARA DESENVOLVIMENTO, DELETAR DEPOIS
def todas_sessoes():
    return sessoes.todas()

@router.get('/{id_usuario}')
def get_dados_usuario(id_usuario: int):
    dto = dict()
    usuario = RepositorioUsuario.find_one(id_usuario)
    if usuario is not None:
        dto = usuario.dto()
    return dto
