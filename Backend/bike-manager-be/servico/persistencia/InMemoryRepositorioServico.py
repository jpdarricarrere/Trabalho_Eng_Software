from typing import Optional

from ..Servico import Servico
from ..TipoServico import TipoServico
from .IRepositorioServico import IRepositorioServico

# Dicionario mapeado pela id da bicicleta
_servicos = {
    0: Servico(
        id=0,
        nome="Joao",
        categoria="Eletricista",
        telefone="0800.0001",
        email="joao@email.com",
        link_imagem="https://irp-cdn.multiscreensite.com/0c02236a/dms3rep/multi/ep%2Bver.jpeg",
        contratado=False,
    ),
    1: Servico(
        id=1,
        nome="Rafael",
        categoria="Pedreiro",
        telefone="0800.0002",
        email="rafael@email.com",
        link_imagem="https://st.depositphotos.com/1000291/3330/i/600/depositphotos_33303707-stock-photo-construction-mason-worker-bricklayer.jpg",
        contratado=False,
    ),
    2: Servico(
        id=2,
        nome="Pedro",
        categoria="Padeiro",
        telefone="0800.0003",
        email="pedro@email.com",
        link_imagem="https://conteudo.imguol.com.br/c/bol/entretenimento/ca/2016/07/07/8jul2016---padeiro-mario-francisco-dos-santos-exibe-uma-de-suas-delicias-preparadas-na-padaria-santa-tereza-no-centro-de-sao-paulo-1467941686800_300x420.jpg",
        contratado=False,
    ),
    3: Servico(
        id=3,
        nome="Vitor",
        categoria="Mecanico",
        telefone="0800.0004",
        email="vitor@email.com",
        link_imagem="https://sprintec.com.br/wp-content/uploads/2020/11/20-de-dezembro-e-comemorado-o-dia-do-mecanico-5497fef78b4b42b3ce1d80e2eaec919a.jpg",
        contratado=False,
    ),
    4: Servico(
        id=4,
        nome="Marthyna",
        categoria="Encanador",
        telefone="0800.0005",
        email="marthyna@email.com",
        link_imagem="https://certificadocursosonline.com/wp-content/uploads/2019/09/curso-de-encanador.jpg",
        contratado=False,
    ),
    5: Servico(
        id=5,
        nome="Jose",
        categoria="Seguranca",
        telefone="0800.0006",
        email="jose@email.com",
        link_imagem="https://www.verzani.com.br/wp-content/uploads/2021/05/banner-seguranca@2x-1024x504.jpg",
        contratado=False,
    ),
    6: Servico(
        id=6,
        nome="Maria",
        categoria="Jardineiro",
        telefone="0800.0007",
        email="maria@email.com",
        link_imagem="https://russelservicos.com.br/wp-content/uploads/2016/01/jardineiro-hotelaria_2.jpg",
        contratado=False,
    ),
    7: Servico(
        id=7,
        nome="Lucas",
        categoria="Domestico",
        telefone="0800.0008",
        email="lucas@email.com",
        link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg",
        contratado=False,
    ),
    8: Servico(
        id=8,
        nome="Renata",
        categoria="Motorista",
        telefone="0800.0009",
        email="renata@email.com",
        link_imagem="https://licencesolucoes.com.br/wp-content/uploads/2021/08/como-se-tornar-motorista-de-aplicativo.jpeg",
        contratado=False,
    ),
    9: Servico(
        id=9,
        nome="Laura",
        categoria="Cuidador",
        telefone="0800.0010",
        email="laura@email.com",
        link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg",
        contratado=False,
    ),
    10: Servico(
        id=10,
        nome="Renato",
        categoria="Enfermeiro",
        telefone="0800.0011",
        email="renato@email.com",
        link_imagem="https://editalconcursosbrasil.com.br/wp-content/uploads/2019/04/enfermeiro.jpg",
        contratado=False,
    ),
}


class InMemoryRepositorioServico(IRepositorioServico):

    def get_all():
        return list(_servicos.values())[:]

    def find(categoria: str):
        encontrados = list(_servicos.values())[:]

        if categoria != '':
            encontrados = [
                bike for bike in encontrados if categoria in bike.categoria]

        return encontrados

    def find_one(id: int) -> Optional[Servico]:
        bike = None
        if id in _servicos:
            bike = _servicos.get(id)
        return bike

    def save(bike: Servico) -> Servico:
        if bike.get_id() == None:
            nova_id = len(_servicos)
            bike.set_id(nova_id)
        _servicos[bike.get_id()] = bike
        return bike

    def delete(id: int) -> None:
        if id in _servicos:
            del _servicos[id]
