import pytest
from src.models import ContaBancaria

def test_transferencia_valida():
    conta_origem = ContaBancaria("João",100)
    conta_destino = ContaBancaria("Maria",100)
    conta_origem.transferir(conta_destino,50)

    assert conta_origem.saldo == 50
    assert conta_destino.saldo == 150

def test_tranferencia_saldo_insuficiente():
    conta_origem = ContaBancaria("João",100)
    conta_destino = ContaBancaria("Maria",100)

    with pytest.raises(ValueError):
        conta_origem.transferir(conta_destino,150)

def test_historico_transacoes():
    conta = ContaBancaria("João",100)
    conta.depositar(100)
    conta.sacar(50)

    assert conta.historico == ["Deposito de +100","Saque de 50"]
    assert len(conta.historico) == 2
    assert conta.historico[0] == "Deposito de +100"
    assert conta.historico[1] == "Saque de 50"
    