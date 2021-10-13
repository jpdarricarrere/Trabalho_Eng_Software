from ..Bike import Bike 
from ..TipoBike import TipoBike

_all_bikes = [
    Bike(id=1, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=2, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=3, alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=4, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=5, alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=6, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=7, alugada=False, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=8, alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=9, alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
    Bike(id=10, alugada=True, em_manutencao=False, tipo=TipoBike.urbana, num_marchas=5, ano=2020, aro=7, id_adm=1),
]

class MockRepositorioBike():

    def find():
        return _all_bikes
