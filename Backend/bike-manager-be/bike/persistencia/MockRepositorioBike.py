from ..Bike import Bike 
from ..TipoBike import TipoBike
from .IRepositorioBike import IRepositorioBike

_all_bikes = [
    Bike(id=1, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=2, alugada=False, em_manutencao=True, tipo=TipoBike.transporte, num_marchas=4, ano=2017, aro=6, id_adm=1),
    Bike(id=3, alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=6, ano=2021, aro=5, id_adm=1),
    Bike(id=4, alugada=False, em_manutencao=False, tipo=TipoBike.transporte, num_marchas=6, ano=2019, aro=8, id_adm=1),
    Bike(id=5, alugada=True, em_manutencao=False, tipo=TipoBike.transporte, num_marchas=5, ano=2017, aro=7, id_adm=1),
    Bike(id=6, alugada=False, em_manutencao=True, tipo=TipoBike.corrida, num_marchas=5, ano=2019, aro=7, id_adm=1),
    Bike(id=7, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=6, ano=2018, aro=6, id_adm=1),
    Bike(id=8, alugada=True, em_manutencao=False, tipo=TipoBike.corrida, num_marchas=4, ano=2018, aro=6, id_adm=1),
    Bike(id=9, alugada=True, em_manutencao=False, tipo=TipoBike.corrida, num_marchas=4, ano=2020, aro=7, id_adm=1),
    Bike(id=10, alugada=True, em_manutencao=False, tipo=TipoBike.corrida, num_marchas=5, ano=2021, aro=5, id_adm=1),
]

class MockRepositorioBike(IRepositorioBike):

    def get_all():
        return _all_bikes[:]
    
    def find(tipo: TipoBike, marchas: int, aro: int):
        encontradas = _all_bikes[:]

        if tipo is not None:
            encontradas = [bike for bike in encontradas if bike.get_tipo() == tipo]

        if marchas is not None:
            encontradas = [bike for bike in encontradas if bike.get_marchas() == marchas]

        if aro is not None:
            encontradas = [bike for bike in encontradas if bike.get_aro() == aro]

        return encontradas 
