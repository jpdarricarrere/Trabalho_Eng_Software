from datetime import datetime
from typing import Optional

from ..Usuario import Usuario
from ..TipoUsuario import TipoUsuario
from .IRepositorioUsuario import IRepositorioUsuario

_usuarios = {
    0: Usuario(0, TipoUsuario.ADMIN, "Admin1", datetime(1970, 1, 1), "adm1@bikes.com", "12345"),
    1: Usuario(1, TipoUsuario.ENTREGADOR, "Entregador1", datetime(1990, 12, 31), "entregador1@bikes.com", "senha"),
    2: Usuario(2, TipoUsuario.CLIENTE, "Cliente1", datetime(2000, 5, 12), "cliente1@bikes.com", "12052000"),
}

class InMemoryRepositorioUsuario(IRepositorioUsuario):
    
    def get_all():
        return list(_usuarios.values())[:] 

    def find_one(id: int) -> Optional[Usuario]:
        usuario = None 
        if id in _usuarios:
            usuario = _usuarios.get(id)
        return usuario

    def save(usuario: Usuario):     # Pode ser tanto create (caso id == None) quanto update (caso tenha id existente)
        if usuario.get_id() == None:
            nova_id = len(_usuarios)
            usuario.set_id(nova_id)
        _usuarios[usuario.id] = usuario
        return usuario
