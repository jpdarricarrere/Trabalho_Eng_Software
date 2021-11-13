from enum import Enum 

class TipoUsuario(Enum):
    ADMIN = 'admin'
    CLIENTE = 'cliente'
    ENTREGADOR = 'entregador'