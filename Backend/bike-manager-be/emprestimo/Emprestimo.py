from datetime import datetime

class Emprestimo:

    def __init__(self, id: int, id_adm: int, id_cliente: int, id_levador: int, id_buscador: int, id_bicicleta: int, inicio: datetime, fim: datetime, quilometragem: int, recebida: bool, paga: bool):
        self.set_id(id)
        self.set_id_adm(id_adm) 
        self.set_id_cliente(id_cliente) 
        self.set_id_levador(id_levador)
        self.set_id_buscador(id_buscador)
        self.set_id_bicicleta(id_bicicleta)
        self.set_inicio(datetime.fromtimestamp(inicio.timestamp()))
        self.set_fim(datetime.fromtimestamp(fim.timestamp()))
        self.set_quilometragem(quilometragem)
        self.set_recebida(recebida)
        self.set_paga(paga) 

    def get_id(self) -> int:
        return self.id 

    def set_id(self, novo_id: int) -> None:
        self.id = novo_id

    def get_id_adm(self) ->  int:
        return self.id_adm 
    
    def set_id_adm(self, novo_id_adm: int) -> None:
        self.id_adm = novo_id_adm

    def get_id_cliente(self) -> int:
        return self.id_cliente

    def set_id_cliente(self, novo_id_cliente: int) -> None:
        self.id_cliente = novo_id_cliente

    def get_id_levador(self) -> int:
        return self.id_levador

    def set_id_levador(self, novo_id_levador: int) -> None:
        self.id_levador = novo_id_levador

    def get_id_buscador(self) -> int:
        return self.id_buscador

    def set_id_buscador(self, novo_id_buscador: int) -> None:
        self.id_buscador = novo_id_buscador

    def get_id_bicicleta(self) -> int:
        return self.id_bicicleta

    def set_id_bicicleta(self, novo_id_bicicleta: int) -> None:
        self.id_bicicleta = novo_id_bicicleta

    def get_inicio(self) -> datetime:
        return datetime.fromtimestamp(self.inicio.timestamp())

    def set_inicio(self, novo_inicio: datetime) -> None:
        self.inicio = datetime.fromtimestamp(novo_inicio.timestamp())

    def get_fim(self) -> datetime:
        return datetime.fromtimestamp(self.fim.timestamp())

    def set_fim(self, novo_fim: datetime) -> None:
        self.fim = datetime.fromtimestamp(novo_fim.timestamp())

    def get_quilometragem(self) -> int:
        return self.quilometragem

    def set_quilometragem(self, nova_quilometragem: int) -> None:
        self.quilometragem = nova_quilometragem

    def get_recebida(self) -> bool:
        return self.recebida

    def set_recebida(self, novo_recebida: bool) -> None:
        self.recebida = novo_recebida

    def get_paga(self) -> bool:
        return self.paga

    def set_paga(self, novo_paga: bool) -> None:
        self.paga = novo_paga

