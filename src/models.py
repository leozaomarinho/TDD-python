
class ContaBancaria:
    def __init__(self,titular:str, saldo:float = 0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <=0:
            raise ValueError("Valor do deposito deve ser positivo.")
            self.saldo+= valor

    def sacar(self,valor: float):
        if valor > self.saldo:
            raise ValueError ("Saldo insuficiente.")
        self.saldo -= valor