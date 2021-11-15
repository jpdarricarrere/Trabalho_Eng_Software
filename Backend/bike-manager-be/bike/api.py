from fastapi import APIRouter

from .TipoBike import TipoBike
from .Bike import Bike
from .ServicoBike import ServicoBike

from .integracao.DTOsBikesRequest import DTOCriarBike, DTOAtualizarBike

from .persistencia.InMemoryRepositorioBike import InMemoryRepositorioBike as RepositorioBike

servico = ServicoBike()

router = APIRouter(
    prefix="/bikes",
    tags=['bikes']
) 

@router.get("/")
def get_bikes(tipo: TipoBike = None, nome: str = "", modelo: str = "", marchas: int = None, aro: int = None):
    print(f'Processando pesquisa por tipo: {tipo}, nome: {nome}, modelo: {modelo}, marchas: {marchas}, aro: {aro}')
    encontradas = RepositorioBike.find(tipo, nome, modelo, marchas, aro)
    return encontradas

# Create
@router.post('/')
def cria_bike(dados: DTOCriarBike):
    nova_bike = Bike(None, dados.nome, dados.modelo, dados.link_imagem, False, False, dados.tipo, dados.num_marchas, dados.ano, dados.aro, dados.id_adm)
    bike_salva = RepositorioBike.save(nova_bike)
    return bike_salva

# Read
@router.get('/{id_bike}')
def get_dados_bike(id_bike: int):
    bike = RepositorioBike.find_one(id_bike)
    return bike 

# Update
@router.put('/{id_bike}')
def atualiza_bike(id_bike: int, dados: DTOAtualizarBike):
    atual = RepositorioBike.find_one(id_bike)

    n_nome = dados.nome if dados.nome is not None else atual.nome 
    n_modelo = dados.modelo if dados.modelo is not None else atual.modelo 
    n_link_imagem = dados.link_imagem if dados.link_imagem is not None else atual.link_imagem
    n_tipo = dados.tipo if dados.tipo is not None else atual.tipo
    n_num_marchas = dados.num_marchas if dados.num_marchas is not None else atual.num_marchas
    n_ano = dados.ano if dados.ano is not None else atual.ano
    n_aro = dados.aro if dados.aro is not None else atual.aro
    n_id_adm = dados.id_adm if dados.id_adm is not None else atual.id_adm

    n_bike = Bike(id_bike, n_nome, n_modelo, n_link_imagem, atual.alugada, atual.em_manutencao, n_tipo, n_num_marchas, n_ano, n_aro, n_id_adm)

    bike_persistida = RepositorioBike.save(n_bike)

    return bike_persistida

# Delete
@router.delete('/{id_bike}')
def deleta_bike(id_bike: int):
        RepositorioBike.delete(id_bike)


    