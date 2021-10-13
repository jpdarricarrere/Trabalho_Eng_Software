from .TipoBike import TipoBike

class Bike:

    def __init__(self, id: int, alugada: bool, em_manutencao: bool, tipo: TipoBike, num_marchas: int, ano: int, aro: int, id_adm: int):
        self._id = id
        self._alugada = alugada
        self._em_manutencao = em_manutencao
        self._tipo = tipo 
        self._num_marchas = num_marchas 
        self._ano = ano 
        self._aro = aro 
        self._id_adm = id_adm
    
    def set_id(self, id: int):
        self._id = id 

    def get_id(self):
        return self._id 

    def set_alugada(self, alugada: bool):
        self._alugada = alugada
    
    def get_alugada(self):
        return self._alugada
    
    def set_manutencao(self, em_manutencao: bool):
        self._em_manutencao = em_manutencao
    
    def get_manutencao(self):
        return self._em_manutencao

    def set_tipo(self, tipo: TipoBike):
        self._tipo = tipo 
    
    def get_tipo(self):
        return self._tipo
    
    def set_marchas(self, num_marchas: int):
        self._num_marchas = num_marchas
    
    def get_marchas(self):
        return self._num_marchas
    
    def set_ano(self, ano: int):
        self._ano = ano 
    
    def get_ano(self):
        return self._ano

    def set_aro(self, aro: int):
        self._aro = aro

    def get_aro(self):
        return self._aro 

    def set_id_adm(self, id_adm: int):
        self._id_adm = id_adm

    def get_id_adm(self):
        return self._id_adm
