import pytest  
from src.models import ContaBancaria

def test_criar_conta():
    conta = ContaBancaria("João",100)
    assert conta.titular == "João"
    assert conta.saldo == 100

def test_deposito_valido():
    conta = ContaBancaria("João",100)
    conta.depositar(100)
    assert conta.saldo == 200

def test_deposito_invalido():
    conta = ContaBancaria("João",100)
    with pytest.raises(ValueError):
        conta.depositar(-100)

def test_saque_valido():
    conta = ContaBancaria("João",100)
    conta.sacar(50)
    assert conta.saldo == 50

def test_saque_invalido():
    conta = ContaBancaria("João",100)
    with pytest.raises(ValueError):
        conta.sacar(150)