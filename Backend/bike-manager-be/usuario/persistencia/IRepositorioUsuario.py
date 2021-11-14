from ..Usuario import Usuario
from typing import Optional

class IRepositorioUsuario:

    def get_all():
        raise Exception("Metodo 'get_all' nao implementado por RepositorioUsuario utilizado!")

    def find_one(id: int) -> Optional[Usuario]:
        raise Exception("Metodo 'find_one' nao implementado por RepositorioUsuario utilizado!")

    def save(usuario: Usuario) -> Usuario:
        raise Exception("Metodo 'save' nao implementado por RepositorioUsuario utilizado!")

    def delete(id: int) -> None:
        raise Exception("Metodo 'delete' nao implementado por RepositorioUsuario utilizado!")
