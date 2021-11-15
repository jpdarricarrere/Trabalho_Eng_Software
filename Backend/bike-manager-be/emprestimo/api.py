from fastapi import APIRouter

from .ServicoEmprestimo import ServicoEmprestimo

servico = ServicoEmprestimo()

router = APIRouter(
    prefix = '/emprestimos',
    tags = ["emprestimos"]
)

@router.get('/reserva/{id_bike}')
def reserva_bike(id_bike: int):
    return servico.reserva_bike(id_bike)