from .persistencia.InMemoryRepositorioTrabalhador import InMemoryRepositorioTrabalhador


class ContrataTrabalhador():

    def contrata_trabalhador(self, id: int):
        atual = InMemoryRepositorioTrabalhador.find_one(id)

        if atual.contratado is True:
            # o que vai ser definido aqui? msg de erro? tratamento de caso especial?
            return None

        atual.contratado = True
        bike_persistida = InMemoryRepositorioTrabalhador.save(atual)
        return bike_persistida

    def demite_trabalhador(self, id: int):
        atual = InMemoryRepositorioTrabalhador.find_one(id)
        atual.contratado = False
        bike_persistida = InMemoryRepositorioTrabalhador.save(atual)

        return bike_persistida
