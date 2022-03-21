from fastapi import APIRouter

from .TipoTrabalhador import TipoTrabalhador
from .Trabalhador import Trabalhador
from .ContrataTrabalhador import ContrataTrabalhador

from .integracao.DTOsBikesRequest import DTOCriarTrabalhador, DTOAtualizarTrabalhador

from .persistencia.InMemoryRepositorioTrabalhador import InMemoryRepositorioTrabalhador

servico = ContrataTrabalhador()

router = APIRouter(
    prefix="/trabalhadores",
    tags=['trabalhadores']
)


@router.get("/")
def get_trabalhadores(
    categoria: str = "",
):
    print(
        f'Processando pesquisa por categoria: {categoria}')
    encontrados = InMemoryRepositorioTrabalhador.find(categoria)
    return encontrados

# Create


@router.post('/')
def cria_trabalhador(dados: DTOCriarTrabalhador):
    novo_trabalhador = Trabalhador(
        None,
        dados.nome,
        dados.telefone,
        dados.email,
        dados.categoria,
        dados.link_imagem,
        False,
    )
    trabalhador_salvo = InMemoryRepositorioTrabalhador.save(novo_trabalhador)
    return trabalhador_salvo

# Read


@router.get('/{id_bike}')
def get_dados_bike(id_bike: int):
    bike = InMemoryRepositorioTrabalhador.find_one(id_bike)
    return bike

# Update


@router.put('/{id_bike}')
def atualiza_bike(id_bike: int, dados: DTOAtualizarTrabalhador):
    atual = InMemoryRepositorioTrabalhador.find_one(id_bike)

    n_nome = dados.nome if dados.nome is not None else atual.nome
    n_telefone = dados.telefone if dados.telefone is not None else atual.telefone
    n_email = dados.email if dados.email is not None else atual.email
    n_categoria = dados.categoria if dados.categoria is not None else atual.categoria
    n_link_imagem = dados.link_imagem if dados.link_imagem is not None else atual.link_imagem

    n_trabalhador = Trabalhador(
        id_bike,
        n_nome,
        n_telefone,
        n_email,
        n_categoria,
        n_link_imagem,
        atual.contratado,
    )

    trabalhador_persistido = InMemoryRepositorioTrabalhador.save(n_trabalhador)

    return trabalhador_persistido

# Delete


@router.delete('/{id_bike}')
def deleta_bike(id_bike: int):
    InMemoryRepositorioTrabalhador.delete(id_bike)
