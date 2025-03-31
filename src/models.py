
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

class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self,titular:str,saldo =0):
        if titular in self.contas:
            raise ValueError("Conta já existe.")
        self.contas[titular] = ContaBancaria(titular,saldo)
    
    def buscar_conta(self,titular:str):
        if titular not in self.contas:
            raise ValueError("Conta não encontrada.")
        return self.contas[titular]

    def transferir(self,titular_origem:str,titular_destino:str,valor:float):
        
        if titular_origem not in self.contas or titular_destino not in self.contas:
            raise ValueError("Conta não encontrada.")
        
        conta_origem = self.buscar_conta(titular_origem)
        conta_destino = self.buscar_conta(titular_destino)
        conta_origem.transferir(conta_destino,valor)