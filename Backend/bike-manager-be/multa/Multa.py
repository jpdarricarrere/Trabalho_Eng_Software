
class Multa:

    def __init__(self, id: int, id_emprestimo: int, valor: int):
        self.set_id(id) 
        self.set_id_emprestimo(id_emprestimo)
        self.set_valor(valor) 

    def get_id(self) -> int:
        return self.id 

    def set_id(self, novo_id: int) -> None:
        self.id = novo_id

    def get_id_emprestimo(self) -> int:
        return self.id_emprestimo

    def set_id_emprestimo(self, novo_id_emprestimo: int) -> None:
        self.id_emprestimo = novo_id_emprestimo

    def get_valor(self) -> int:
        return self.valor 

    def set_valor(self, novo_valor) -> None:
        self.valor = novo_valor