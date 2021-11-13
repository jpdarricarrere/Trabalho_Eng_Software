from fastapi import APIRouter 
from .Sessao import Sessao
from .persistencia.InMemoryRepositorioUsuario import InMemoryRepositorioUsuario as RepositorioUsuario

router = APIRouter(
    prefix = '/usuarios'
)

sessoes = Sessao()

@router.get("/")
def get_usuarios():
    encontrados = RepositorioUsuario.get_all()
    return [u.dto() for u in encontrados]

@router.get('/login')       # TODO: Mudar isso para POST
def login(email: str = '', senha: str = '') -> dict:
    if email == '' or senha == '':
        return dict()

    return sessoes.login(email, senha)

@router.get('/logout')
def logout(email: str = '', token: str = ''):
    if email == '' or token == '':
        return 

    sessoes.logout(email, token)

@router.get('/todas_sessoes')
def todas_sessoes():
    return sessoes.todas()