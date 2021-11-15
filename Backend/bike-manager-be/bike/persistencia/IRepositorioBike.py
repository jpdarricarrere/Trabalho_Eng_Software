from typing import Optional

from ..Bike import Bike
from ..TipoBike import TipoBike

class IRepositorioBike:

    def get_all():
        raise Exception("Metodo 'get_all' nao implementado por RepositorioBike utilizado!")

    def find(tipo: TipoBike, nome: str, modelo: str, marchas: int, aro: int):
        raise Exception("Metodo 'find' nao implementado por RepositorioBike utilizado!")

    def find_one(id: int) -> Optional[Bike]:
        raise Exception("Metodo 'find_one' nao implementado por RepositorioBike utilizado!")

    def save(bike: Bike) -> Bike:
        raise Exception("Metodo 'save' nao implementado por RepositorioBike utilizado!")

    def delete(id: int) -> None:
        raise Exception("Metodo 'delete' nao implementado por RepositorioBike utilizado!")

    
