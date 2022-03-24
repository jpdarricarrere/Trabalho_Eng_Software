from typing import Optional

from ..Servico import Servico
from ..TipoServico import TipoServico


class IRepositorioServico:

    def get_all():
        raise Exception(
            "Metodo 'get_all' nao implementado por RepositorioServico utilizado!")

    def find(categoria: str):
        raise Exception(
            "Metodo 'find' nao implementado por RepositorioServico utilizado!")

    def find_one(id: int) -> Optional[Servico]:
        raise Exception(
            "Metodo 'find_one' nao implementado por RepositorioServico utilizado!")

    def save(bike: Servico) -> Servico:
        raise Exception(
            "Metodo 'save' nao implementado por RepositorioServico utilizado!")

    def delete(id: int) -> None:
        raise Exception(
            "Metodo 'delete' nao implementado por RepositorioServico utilizado!")
