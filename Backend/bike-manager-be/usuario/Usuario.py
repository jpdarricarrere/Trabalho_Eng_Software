from datetime import datetime
from .TipoUsuario import TipoUsuario

class Usuario:

    def __init__(self, id: int, tipo: TipoUsuario, nome: str, data_nascimento: datetime, email: str, senha: str):
        self.set_id(id)
        self.set_tipo(tipo)
        self.set_nome(nome)
        self.set_data_nascimento(data_nascimento)
        self.set_email(email)
        self.set_senha(senha)

    def get_id(self) -> int:
        return self.id 

    def set_id(self, novo_id: int) -> None:
        self.id = novo_id

    def get_tipo(self) -> TipoUsuario:
        return self.tipo 

    def set_tipo(self, novo_tipo: TipoUsuario) -> None:
        self.tipo = novo_tipo

    def get_nome(self) -> str:
        return self.nome 
    
    def set_nome(self, novo_nome: str) -> None:
        self.nome = novo_nome

    def get_data_nascimento(self) -> datetime:
        return datetime.fromtimestamp(self.data_nascimento.timestamp())

    def set_data_nascimento(self, nova_data: datetime) -> None:
        self.data_nascimento = datetime.fromtimestamp(nova_data.timestamp())

    def get_email(self) -> str:
        return self.email

    def set_email(self, novo_email: str) -> None:
        self.email = novo_email

    def get_senha(self) -> str:
        return self.senha

    def set_senha(self, nova_senha: str) -> None:
        self.senha = nova_senha
