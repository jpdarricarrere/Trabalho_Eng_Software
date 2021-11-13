from datetime import datetime

class Emprestimo:

    def __init__(self, id: int, id_adm: int, id_cliente: int, id_levador: int, id_buscador: int, id_bicicleta: int, inicio: datetime, fim: datetime, quilometragem: int, recebida: bool, paga: bool):
        self.id = id,
        self.id_adm = id_adm 
        self.id_cliente = id_cliente 
        self.id_levador = id_levador
        self.id_buscador = id_buscador
        self.id_bicicleta = id_bicicleta
        self.inicio = datetime.fromtimestamp(inicio.timestamp())
        self.fim = datetime.fromtimestamp(fim.timestamp())
        self.quilometragem = quilometragem
        self.recebida = recebida
        self.paga = paga 

    @property 
    def id(self) -> int:
        return self.id 

    @id.setter 
    def id(self, novo_id: int) -> None:
        self.id = novo_id

    @property 
    def id_adm(self) ->  int:
        return self.id_adm 
    
    @id_adm.setter 
    def id_adm(self, novo_id_adm: int) -> None:
        self.id_adm = novo_id_adm

    @property 
    def id_cliente(self) -> int:
        return self.id_cliente

    @id_cliente.setter 
    def id_cliente(self, novo_id_cliente: int) -> None:
        self.id_cliente = novo_id_cliente

    @property 
    def id_levador(self) -> int:
        return self.id_levador

    @id_levador.setter 
    def id_levador(self, novo_id_levador: int) -> None:
        self.id_levador = novo_id_levador

    @property 
    def id_buscador(self) -> int:
        return self.id_buscador

    @id_buscador.setter 
    def id_buscador(self, novo_id_buscador: int) -> None:
        self.id_buscador = novo_id_buscador

    @property 
    def id_bicicleta(self) -> int:
        return self.id_bicicleta

    @id_bicicleta.setter 
    def id_bicicleta(self, novo_id_bicicleta: int) -> None:
        self.id_bicicleta = novo_id_bicicleta

    @property 
    def inicio(self) -> datetime:
        return datetime.fromtimestamp(self.inicio.timestamp())

    @inicio.setter 
    def inicio(self, novo_inicio: datetime) -> None:
        self.inicio = datetime.fromtimestamp(novo_inicio.timestamp())

    @property 
    def fim(self) -> datetime:
        return datetime.fromtimestamp(self.fim.timestamp())

    @fim.setter 
    def fim(self, novo_fim: datetime) -> None:
        self.fim = datetime.fromtimestamp(novo_fim.timestamp())

    @property 
    def quilometragem(self) -> int:
        return self.quilometragem

    @quilometragem.setter
    def quilometragem(self, nova_quilometragem: int) -> None:
        self.quilometragem = nova_quilometragem

    @property 
    def recebida(self) -> bool:
        return self.recebida

    @recebida.setter 
    def recebida(self, novo_recebida: bool) -> None:
        self.recebida = novo_recebida

    @property 
    def paga(self) -> bool:
        return self.paga

    @paga.setter 
    def paga(self, novo_paga: bool) -> None:
        self.paga = novo_paga

