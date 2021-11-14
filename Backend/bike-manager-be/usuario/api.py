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
    print(f'{dados.email}, {dados.senha}')
    if dados.email == '' or dados.senha == '':
        return dict()

    return sessoes.login(dados.email, dados.senha)

@router.get('/logout')
def logout(email: str = '', token: str = ''):
    if email == '' or token == '':
        return 

    sessoes.logout(email, token)

@router.get('/todas_sessoes')
def todas_sessoes():
    return sessoes.todas()