from datetime import datetime

class Usuario:

    def __init__(self, id: int, nome: str, data_nascimento: datetime, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
        self.senha = senha

    @property 
    def id(self) -> int:
        return self.id 

    @id.setter 
    def id(self, novo_id: int) -> None:
        self.id = novo_id

    @property 
    def nome(self) -> str:
        return self.nome 
    
    @nome.setter 
    def nome(self, novo_nome: str) -> None:
        self.nome = novo_nome

    @property 
    def data_nascimento(self) -> datetime:
        return datetime.fromtimestamp(self.data_nascimento.timestamp())

    @data_nascimento.setter
    def data_nascimento(self, nova_data: datetime) -> None:
        self.data_nascimento = datetime.fromtimestamp(nova_data.timestamp())

    @property 
    def email(self) -> str:
        return self.email

    @email.setter 
    def email(self, novo_email: str) -> None:
        self.email = novo_email

    @property 
    def senha(self) -> str:
        return self.senha

    @senha.setter 
    def senha(self, nova_senha: str) -> None:
        self.senha = nova_senha
