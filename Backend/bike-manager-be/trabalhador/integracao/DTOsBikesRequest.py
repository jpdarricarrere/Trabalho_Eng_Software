from pydantic import BaseModel
from typing import Optional
from ..TipoTrabalhador import TipoTrabalhador


class DTOCriarTrabalhador(BaseModel):
    nome: str
    telefone: str
    email: str
    categoria: str
    link_imagem: str
    contratado: bool


class DTOAtualizarTrabalhador(BaseModel):
    nome: Optional[str]
    telefone: Optional[str]
    email: Optional[str]
    categoria: Optional[str]
    link_imagem: Optional[str]
    contratado: Optional[bool]
