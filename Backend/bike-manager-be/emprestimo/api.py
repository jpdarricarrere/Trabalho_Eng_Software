from fastapi import APIRouter

from .ServicoEmprestimo import ServicoEmprestimo

servico = ServicoEmprestimo()

router = APIRouter(
    prefix='/emprestimos',
    tags=["emprestimos"]
)


@router.get('/reserva/{id}')
def contrata_trabalhador(id: int):
    return servico.contrata_trabalhador(id)
