from fastapi import APIRouter

from .TipoServico import TipoServico
from .Servico import Servico
from .ContrataServico import ContrataServico

from .integracao.DTOsBikesRequest import DTOCriarServico, DTOAtualizarServico

from .persistencia.InMemoryRepositorioServico import InMemoryRepositorioServico

servico = ContrataServico()

router = APIRouter(
    prefix="/servicos",
    tags=['servicos']
)


@router.get("/")
def get_servicos(
    categoria: str = "",
):
    print(
        f'Processando pesquisa por categoria: {categoria}')
    encontrados = InMemoryRepositorioServico.find(categoria)
    return encontrados

# Create


@router.post('/')
def cria_servico(dados: DTOCriarServico):
    novo_servico = Servico(
        None,
        dados.nome,
        dados.telefone,
        dados.email,
        dados.categoria,
        dados.link_imagem,
        False,
    )
    servico_salvo = InMemoryRepositorioServico.save(novo_servico)
    return servico_salvo

# Read


@router.get('/{id_bike}')
def get_dados_bike(id_bike: int):
    bike = InMemoryRepositorioServico.find_one(id_bike)
    return bike

# Update


@router.put('/{id_bike}')
def atualiza_bike(id_bike: int, dados: DTOAtualizarServico):
    atual = InMemoryRepositorioServico.find_one(id_bike)

    n_nome = dados.nome if dados.nome is not None else atual.nome
    n_telefone = dados.telefone if dados.telefone is not None else atual.telefone
    n_email = dados.email if dados.email is not None else atual.email
    n_categoria = dados.categoria if dados.categoria is not None else atual.categoria
    n_link_imagem = dados.link_imagem if dados.link_imagem is not None else atual.link_imagem

    n_servico = Servico(
        id_bike,
        n_nome,
        n_telefone,
        n_email,
        n_categoria,
        n_link_imagem,
        atual.contratado,
    )

    servico_persistido = InMemoryRepositorioServico.save(n_servico)

    return servico_persistido

# Delete


@router.delete('/{id_bike}')
def deleta_bike(id_bike: int):
    InMemoryRepositorioServico.delete(id_bike)
