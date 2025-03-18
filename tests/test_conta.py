import pytest
from src.models import ContaBancaria
from unittest.mock import patch

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

def test_historico_transacoes(conta):
    conta.depositar(100)
    conta.sacar(50)

    assert conta.historico == ["Deposito de +100","Saque de 50"]

def test_deposito_valido(conta):
    conta.depositar(100)

    assert conta.saldo == 200

@patch("src.models.ContaBancaria.sacar") # Mockando o metodo sacar
def test_mock_saque(mock_sacar, conta):
    mock_sacar.return_value = None
    conta.sacar(50)

    mock_sacar.assert_called_once_with(50) #Verifica se o metodo foi chamado com o valor correto

def test_mockar_deposito(mocker,conta):
    mock_deposito = mocker.patch.object(conta,"depositar",return_value=None) #Mockando o metodo depositar
    conta.depositar(100)

    mock_deposito.assert_called_once_with(100) #Verifica se o metodo foi chamado com o valor correto

