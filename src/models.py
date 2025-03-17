
class ContaBancaria:
    def __init__(self,titular:str, saldo:float = 0.0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor: float):
        if valor <=0:
            raise ValueError("Valor do deposito deve ser positivo.")
        self.saldo+= valor
        self.historico.append(f"Deposito de +{valor}")

    def sacar(self,valor: float):
        if valor > self.saldo:
            raise ValueError ("Saldo insuficiente.")
        self.saldo -= valor
        self.historico.append(f"Saque de {valor}")

    def transferir(self, conta_destino, valor: float):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        conta_destino.saldo += valor
        self.historico.append(f"Transferencia de -{valor} para {conta_destino.titular}")
        conta_destino.historico.append(f"Transferencia de +{valor} de {self.titular}")