from .persistencia.InMemoryRepositorioBike import InMemoryRepositorioBike as RepositorioBike

class ServicoBike():

    def aluga_bike(self, id:int):
        atual = RepositorioBike.find_one(id)

        if atual.alugada is True or atual.em_manutencao is True:
            #o que vai ser definido aqui? msg de erro? tratamento de caso especial?
            return None

        atual.alugada = True
        bike_persistida = RepositorioBike.save(atual)
        return bike_persistida

    def desaluga_bike(self, id:int):
        atual = RepositorioBike.find_one(id)
        atual.alugada = False
        bike_persistida = RepositorioBike.save(atual)
        
        return bike_persistida

    def manutencao_bike(self, id:int):
        atual = RepositorioBike.find_one(id)

        if atual.alugada is True:
            return None

        atual.em_manutencao = True
        bike_persistida = RepositorioBike.save(atual)   
        return bike_persistida

    def desmanutencao_bike(self, id:int):
        atual = RepositorioBike.find_one(id)
            
        atual.em_manutencao = False
        bike_persistida = RepositorioBike.save(atual) 
        return bike_persistida
