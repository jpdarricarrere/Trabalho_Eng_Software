from fastapi import APIRouter
from .TipoBike import TipoBike
from .persistencia.MockRepositorioBike import MockRepositorioBike as RepositorioBike

router = APIRouter(
    prefix="/bikes"
) 

@router.get("/")
def get_bikes(tipo: TipoBike = None, nome: str = "", modelo: str = "", marchas: int = None, aro: int = None):
    print(f'Processando pesquisa por tipo: {tipo}, nome: {nome}, modelo: {modelo}, marchas: {marchas}, aro: {aro}')
    encontradas = RepositorioBike.find(tipo, nome, modelo, marchas, aro)
    return encontradas

