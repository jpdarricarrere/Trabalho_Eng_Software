from fastapi import APIRouter

from .ServicoEmprestimo import ServicoEmprestimo

servico = ServicoEmprestimo()

router = APIRouter(
    prefix='/emprestimos',
    tags=["emprestimos"]
)


@router.get('/reserva/{id}')
def contrata_servico(id: int):
    return servico.contrata_servico(id)
