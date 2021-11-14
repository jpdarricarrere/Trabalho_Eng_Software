from datetime import datetime

from .Usuario import Usuario
from .TipoUsuario import TipoUsuario
from .persistencia.InMemoryRepositorioUsuario import InMemoryRepositorioUsuario as RepositorioUsuario

class ServicoUsuario:
    
    def criar(tipo: TipoUsuario, nome: str, ano_nascimento: int, mes_nascimento: int, dia_nascimento: int, email: str, senha: str):
        data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
        novo_usuario = Usuario(None, tipo, nome, data_nascimento, email, senha)

        usuario_persistido = RepositorioUsuario.save(novo_usuario)

        return usuario_persistido