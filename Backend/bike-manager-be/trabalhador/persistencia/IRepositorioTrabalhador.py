from typing import Optional

from ..Trabalhador import Trabalhador
from ..TipoTrabalhador import TipoTrabalhador


class IRepositorioTrabalhador:

    def get_all():
        raise Exception(
            "Metodo 'get_all' nao implementado por RepositorioTrabalhador utilizado!")

    def find(categoria: str):
        raise Exception(
            "Metodo 'find' nao implementado por RepositorioTrabalhador utilizado!")

    def find_one(id: int) -> Optional[Trabalhador]:
        raise Exception(
            "Metodo 'find_one' nao implementado por RepositorioTrabalhador utilizado!")

    def save(bike: Trabalhador) -> Trabalhador:
        raise Exception(
            "Metodo 'save' nao implementado por RepositorioTrabalhador utilizado!")

    def delete(id: int) -> None:
        raise Exception(
            "Metodo 'delete' nao implementado por RepositorioTrabalhador utilizado!")
