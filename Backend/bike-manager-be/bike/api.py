from fastapi import APIRouter

from .TipoBike import TipoBike
from .Bike import Bike

from .integracao.DTOsBikesRequest import DTOCriarBike

from .persistencia.InMemoryRepositorioBike import InMemoryRepositorioBike as RepositorioBike

router = APIRouter(
    prefix="/bikes"
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
def atualiza_bike(id: int, nome: str, modelo: str, tipo: TipoBike, num_marchas: int, ano: int, aro: int):
    atual = RepositorioBike.find_one(id)

    n_modelo = modelo if modelo is not None else atual.modelo 
    n_nome = nome if nome is not None else atual.nome 
    n_tipo = tipo if tipo is not None else atual.tipo
    n_tipo = tipo if tipo is not None else atual.tipo
    n_num_marchas = num_marchas if num_marchas is not None else atual.num_marchas
    n_ano = ano if ano is not None else atual.ano
    n_aro = aro if aro is not None else atual.aro

    n_bike = Bike(id, n_nome, n_modelo, atual.link_imagem, atual.alugada, atual.em_manutencao, n_tipo, n_num_marchas, n_ano, n_aro, atual.id_adm)

    bike_persistida = RepositorioBike.save(n_bike)

    return bike_persistida

# Delete
def deleta_bike(id: int):
        RepositorioBike.delete(id)

def aluga_bike(id:int):
    atual = RepositorioBike.find_one(id)

    if atual.alugada is True or atual.em_manutencao is True:
        #o que vai ser definido aqui? msg de erro? tratamento de caso especial?
        return None

    atual.alugada = True
    bike_persistida = RepositorioBike.save(atual)
    return bike_persistida

def desaluga_bike(id:int):
    atual = RepositorioBike.find_one(id)
    atual.alugada = False
    bike_persistida = RepositorioBike.save(atual)
    
    return bike_persistida

def manutencao_bike(id:int):
    atual = RepositorioBike.find_one(id)

    if atual.alugada is True:
        return None

    atual.em_manutencao = True
    bike_persistida = RepositorioBike.save(atual)   
    return bike_persistida

def desmanutencao_bike(id:int):
    atual = RepositorioBike.find_one(id)
        
    atual.em_manutencao = False
    bike_persistida = RepositorioBike.save(atual) 
    return bike_persistida

    