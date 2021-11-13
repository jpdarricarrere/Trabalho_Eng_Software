from fastapi import APIRouter 
from .persistencia.InMemoryRepositorioUsuario import InMemoryRepositorioUsuario as RepositorioUsuario

router = APIRouter(
    prefix = '/usuarios'
)

@router.get("/")
def get_usuarios():
    encontrados = RepositorioUsuario.get_all()
    return [u.dto() for u in encontrados]