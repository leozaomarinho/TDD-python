class BancoDeDados:
    def obter_saldo(self,titular):
        raise NotImplementedError("Deve ser implementado!")

class ServicoConta:
    def __init__(self,banco:BancoDeDados):
        self.banco = banco

    def verificar_saldo(self,titular):
        return self.banco.obter_saldo(titular)