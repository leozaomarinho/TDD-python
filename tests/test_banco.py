import pytest
from src.models import Banco,ContaBancaria
from unittest.mock import patch

@pytest.fixture
def banco():
    """Fixture para criar um banco com algumas contas para os testes."""
    banco = Banco()
    banco.adicionar_conta("João",1000)
    banco.adicionar_conta("Maria",500)
    return banco

def test_transferencia_sucesso(banco):
    banco.transferir("João", "Maria", 200)
    assert banco.buscar_conta("João").saldo == 800
    assert banco.buscar_conta("Maria").saldo == 700
    assert "Transferencia de -200 para Maria" in banco.buscar_conta("João").historico
    assert "Transferencia de +200 de João" in banco.buscar_conta("Maria").historico

def test_transferencia_conta_inexistente(banco):
    with pytest.raises(ValueError, match="Conta não encontrada"):
        banco.transferir("João", "Inexistente", 200)

def test_adicionar_conta(banco):
    banco.adicionar_conta("Carlos", 2000)
    assert len(banco.contas) == 3
    assert banco.contas["Carlos"].saldo == 2000

def test_buscar_conta(banco):
    conta = banco.buscar_conta("João")
    assert conta.titular == "João"
    assert conta.saldo == 1000
    assert conta.historico == []

def test_buscar_conta_inexistente(banco):
    with pytest.raises(ValueError, match="Conta não encontrada"):
        banco.buscar_conta("Inexistente")

