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

