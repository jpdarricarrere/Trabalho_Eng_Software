
class ServicoEmprestimo():

    def __init__(self):
        self._servico_bike = None

    def set_servico_bike(self, servico_bike):
        self._servico_bike = servico_bike

    def contrata_servico(self, id):
        if self._servico_bike is None:
            raise('ServicoEmprestimo nao possui forma de chega em bikes. Verifique se uma referencia para o servico de bikes foi passada a ele.')

        self._servico_bike.contrata_servico(id)
