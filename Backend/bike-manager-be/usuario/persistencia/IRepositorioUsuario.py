from ..Usuario import Usuario

class IRepositorioUsuario:

    def get_all():
        raise Exception("Metodo 'get_all' nao implementado por RepositorioUsuario utilizado!")

    def find_one(id: int) -> Usuario:
        raise Exception("Metodo 'find_one' nao implementado por RepositorioBike utilizado!")
