from .TipoTrabalhador import TipoTrabalhador


class Trabalhador:

    def __init__(
        self,
        id: int,
        nome: str,
        categoria: str,
        telefone: str,
        email: str,
        link_imagem: str,
        contratado: bool,
    ):
        # vvv NEW VARS vvv
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.telefone = telefone
        self.email = email
        self.link_imagem = link_imagem
        self.contratado = contratado

        # vvv OLD VARS vvv
        #self.modelo = modelo
        #self.em_manutencao = em_manutencao
        #self.tipo = tipo
        #self.num_marchas = num_marchas
        #self.ano = ano
        #self.aro = aro
        #self.id_adm = id_adm
