from ..Bike import Bike 
from ..TipoBike import TipoBike
from .IRepositorioBike import IRepositorioBike

_all_bikes = [
    Bike(id=1, nome="Bicicleta 1", modelo="Modelo1", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=2, nome="Bicicleta 2", modelo="Modelo2", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=False, em_manutencao=True, tipo=TipoBike.transporte, num_marchas=4, ano=2017, aro=6, id_adm=1),
    Bike(id=3, nome="Bicicleta 3", modelo="Modelo3", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=6, ano=2021, aro=5, id_adm=1),
    Bike(id=4, nome="Bicicleta 4", modelo="Modelo4", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=False, em_manutencao=False, tipo=TipoBike.transporte, num_marchas=6, ano=2019, aro=8, id_adm=1),
    Bike(id=5, nome="Bicicleta 5", modelo="Modelo5", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=True, em_manutencao=False, tipo=TipoBike.transporte, num_marchas=5, ano=2017, aro=7, id_adm=1),
    Bike(id=6, nome="Bicicleta 6", modelo="Modelo6", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=False, em_manutencao=True, tipo=TipoBike.corrida, num_marchas=5, ano=2019, aro=7, id_adm=1),
    Bike(id=7, nome="Bicicleta 7", modelo="Modelo7", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=6, ano=2018, aro=6, id_adm=1),
    Bike(id=8, nome="Bicicleta 8", modelo="Modelo8", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=True, em_manutencao=False, tipo=TipoBike.corrida, num_marchas=4, ano=2018, aro=6, id_adm=1),
    Bike(id=9, nome="Bicicleta 9", modelo="Modelo9", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=True, em_manutencao=False, tipo=TipoBike.corrida, num_marchas=4, ano=2020, aro=7, id_adm=1),
    Bike(id=10, nome="Bicicleta 10", modelo="Modelo10", link_imagem="https://d2ul2exfru69gk.cloudfront.net/Custom/Content/Products/13/16/13163_bicicleta-nova-specialized-epic-ht-carbon-29-2020-37241_z4_637288976190418780.jpg", alugada=True, em_manutencao=False, tipo=TipoBike.corrida, num_marchas=5, ano=2021, aro=5, id_adm=1),
]

class MockRepositorioBike(IRepositorioBike):

    def get_all():
        return _all_bikes[:]
    
    def find(tipo: TipoBike, nome: str, modelo: str, marchas: int, aro: int):
        encontradas = _all_bikes[:]

        if tipo is not None:
            encontradas = [bike for bike in encontradas if bike.get_tipo() == tipo]

        if marchas is not None:
            encontradas = [bike for bike in encontradas if bike.get_marchas() == marchas]

        if aro is not None:
            encontradas = [bike for bike in encontradas if bike.get_aro() == aro]

        if nome != '':
            encontradas = [bike for bike in encontradas if nome in bike.get_nome()]

        if modelo != '':
            encontradas = [bike for bike in encontradas if modelo in bike.get_modelo()]

        return encontradas 
