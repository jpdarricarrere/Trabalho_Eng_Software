from fastapi import APIRouter 

from .Sessao import Sessao
from .integracao.DTOLoginRequest import DTOLoginRequest

from .ServicoUsuario import ServicoUsuario
from .integracao.DTOsUsuariosRequest import DTOCriarUsuario, DTOAtualizarUsuario



router = APIRouter(
    prefix = '/usuarios',
    tags = ["usuarios"]
)

sessoes = Sessao()

@router.get("/")
def get_usuarios():
    encontrados = ServicoUsuario.listar_todos()
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

# Create
@router.post('/')
def cria_usuario(dados: DTOCriarUsuario):
    return ServicoUsuario.criar(
        dados.tipo, dados.nome, dados.ano_nascimento, dados.mes_nascimento, dados.dia_nascimento, dados.email, dados.senha
    )

# Read
@router.get('/{id_usuario}')
def get_dados_usuario(id_usuario: int):
    dto = dict()
    usuario = ServicoUsuario.encontrar(id_usuario)
    if usuario is not None:
        dto = usuario.dto()
    return dto

# Update
@router.put('/{id_usuario}')
def atualiza_usuario(id_usuario: int, dados: DTOAtualizarUsuario):
    return ServicoUsuario.atualizar(
        id_usuario, dados.tipo, dados.nome, dados.ano_nascimento, dados.mes_nascimento, dados.dia_nascimento, dados.email, dados.senha
    )
    
# Delete
@router.delete('/{id_usuario}')
def deleta_usuario(id_usuario: int):
    usuario = ServicoUsuario.encontrar(id_usuario)
    if usuario is not None:
        sessoes.invalidar_todas_para_usuario(usuario.get_email())
    return ServicoUsuario.deletar(id_usuario)
