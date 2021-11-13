
class Multa:

    def __init__(self, id: int, id_emprestimo: int, valor: int):
        self.id = id 
        self.id_emprestimo = id_emprestimo
        self.valor = valor 

    @property 
    def id(self) -> int:
        return self.id 

    @id.setter 
    def id(self, novo_id: int) -> None:
        self.id = novo_id

    @property 
    def id_emprestimo(self) -> int:
        return self.id_emprestimo

    @id_emprestimo.setter 
    def id_emprestimo(self, novo_id_emprestimo: int) -> None:
        self.id_emprestimo = novo_id_emprestimo

    @property 
    def valor(self) -> int:
        return self.valor 

    @valor.setter 
    def valor(self, novo_valor) -> None:
        self.valor = novo_valor