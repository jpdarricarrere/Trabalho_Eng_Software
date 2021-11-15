from pydantic import BaseModel 
from typing import Optional 
from ..TipoBike import TipoBike

class DTOCriarBike(BaseModel):
    nome: str
    modelo: str 
    link_imagem: str
    tipo: TipoBike
    num_marchas: int 
    ano: int 
    aro: int 
    id_adm: int 

class DTOAtualizarBike(BaseModel):
    nome: Optional[str]
    modelo: Optional[str]
    link_imagem: Optional[str]
    tipo: Optional[TipoBike]
    num_marchas: Optional[int]
    ano: Optional[int] 
    aro: Optional[int] 
    id_adm: Optional[int] 

