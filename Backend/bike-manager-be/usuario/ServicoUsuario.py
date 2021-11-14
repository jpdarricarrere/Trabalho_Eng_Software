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

    def atualizar(id: int, tipo: TipoUsuario, nome: str, ano_nascimento: int, mes_nascimento: int, dia_nascimento: int, email: str, senha: str):
        atual = RepositorioUsuario.find_one(id)

        n_tipo = tipo if tipo is not None else atual.tipo 
        n_nome = nome if nome is not None else atual.nome 

        atual_data_nasc = atual.get_data_nascimento()
        n_ano = ano_nascimento if ano_nascimento is not None else atual_data_nasc.year
        n_mes = mes_nascimento if mes_nascimento is not None else atual_data_nasc.month
        n_dia = dia_nascimento if dia_nascimento is not None else atual_data_nasc.day
        n_data_nascimento = datetime(n_ano, n_mes, n_dia)

        n_email = email if email is not None else atual.email 
        n_senha = senha if senha is not None else atual.senha

        n_usuario = Usuario(id, n_tipo, n_nome, n_data_nascimento, n_email, n_senha)

        usuario_persistido = RepositorioUsuario.save(n_usuario)

        return usuario_persistido