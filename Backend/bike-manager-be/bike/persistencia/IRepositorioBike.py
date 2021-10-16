from ..TipoBike import TipoBike

class IRepositorioBike:

    def get_all():
        raise Exception("Metodo 'get_all' nao implementado por RepositorioBike utilizado!")

    def find(tipo: TipoBike, nome: str, modelo: str, marchas: int, aro: int):
        raise Exception("Metodo 'find' nao implementado por RepositorioBike utilizado!")
