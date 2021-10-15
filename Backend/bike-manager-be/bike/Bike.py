from .TipoBike import TipoBike

class Bike:

    def __init__(self, id: int, nome: str, modelo: str, link_imagem: str, alugada: bool, em_manutencao: bool, tipo: TipoBike, num_marchas: int, ano: int, aro: int, id_adm: int):
        self._id = id
        self._nome = nome 
        self._modelo = modelo 
        self._link_imagem = link_imagem
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

    def set_nome(self, nome: str):
        self._nome = nome 

    def get_nome(self):
        return self._nome

    def set_modelo(self, modelo: str):
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo

    def set_link_image(self, link_imagem: str):
        self._link_imagem = link_imagem 

    def get_link_imagem(self):
        return self._link_imagem

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
