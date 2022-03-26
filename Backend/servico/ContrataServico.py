from .persistencia.InMemoryRepositorioServico import InMemoryRepositorioServico


class ContrataServico():

    def contrata_servico(self, id: int):
        atual = InMemoryRepositorioServico.find_one(id)

        if atual.contratado is True:
            # o que vai ser definido aqui? msg de erro? tratamento de caso especial?
            return None

        atual.contratado = True
        bike_persistida = InMemoryRepositorioServico.save(atual)
        return bike_persistida

    def demite_servico(self, id: int):
        atual = InMemoryRepositorioServico.find_one(id)
        atual.contratado = False
        bike_persistida = InMemoryRepositorioServico.save(atual)

        return bike_persistida
