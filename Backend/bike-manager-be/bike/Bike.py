from .TipoBike import TipoBike

class Bike:

    def __init__(self, id: int, nome: str, modelo: str, link_imagem: str, alugada: bool, em_manutencao: bool, tipo: TipoBike, num_marchas: int, ano: int, aro: int, id_adm: int):
        self.id = id
        self.nome = nome 
        self.modelo = modelo 
        self.link_imagem = link_imagem
        self.alugada = alugada
        self.em_manutencao = em_manutencao
        self.tipo = tipo 
        self.num_marchas = num_marchas 
        self.ano = ano 
        self.aro = aro 
        self.id_adm = id_adm
    
    def set_id(self, id: int):
        self.id = id 

    def get_id(self):
        return self.id 

    def set_nome(self, nome: str):
        self.nome = nome 

    def get_nome(self):
        return self.nome

    def set_modelo(self, modelo: str):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_link_image(self, link_imagem: str):
        self.link_imagem = link_imagem 

    def get_link_imagem(self):
        return self.link_imagem

    def set_alugada(self, alugada: bool):
        self.alugada = alugada
    
    def get_alugada(self):
        return self.alugada
    
    def set_manutencao(self, em_manutencao: bool):
        self.em_manutencao = em_manutencao
    
    def get_manutencao(self):
        return self.em_manutencao

    def set_tipo(self, tipo: TipoBike):
        self.tipo = tipo 
    
    def get_tipo(self):
        return self.tipo
    
    def set_marchas(self, num_marchas: int):
        self.num_marchas = num_marchas
    
    def get_marchas(self):
        return self.num_marchas
    
    def set_ano(self, ano: int):
        self.ano = ano 
    
    def get_ano(self):
        return self.ano

    def set_aro(self, aro: int):
        self.aro = aro

    def get_aro(self):
        return self.aro 

    def set_id_adm(self, id_adm: int):
        self.id_adm = id_adm

    def get_id_adm(self):
        return self.id_adm
