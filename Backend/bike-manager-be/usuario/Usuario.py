from datetime import datetime
from .TipoUsuario import TipoUsuario

class Usuario:

    def __init__(self, id: int, tipo: TipoUsuario, nome: str, data_nascimento: datetime, email: str, senha: str):
        self._id = id
        self._tipo = tipo
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._email = email
        self._senha = senha

    @property 
    def id(self) -> int:
        return self._id 

    @id.setter 
    def id(self, novo_id: int) -> None:
        self._id = novo_id

    @property 
    def tipo(self) -> TipoUsuario:
        return self._tipo 

    @tipo.setter 
    def tipo(self, novo_tipo: TipoUsuario) -> None:
        self._tipo = novo_tipo

    @property 
    def nome(self) -> str:
        return self._nome 
    
    @nome.setter 
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @property 
    def data_nascimento(self) -> datetime:
        return datetime.fromtimestamp(self._data_nascimento.timestamp())

    @data_nascimento.setter
    def data_nascimento(self, nova_data: datetime) -> None:
        self._data_nascimento = datetime.fromtimestamp(nova_data.timestamp())

    @property 
    def email(self) -> str:
        return self._email

    @email.setter 
    def email(self, novo_email: str) -> None:
        self._email = novo_email

    @property 
    def senha(self) -> str:
        return self._senha

    @senha.setter 
    def senha(self, nova_senha: str) -> None:
        self._senha = nova_senha
