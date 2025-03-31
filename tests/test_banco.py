import pytest
from src.models import Banco,ContaBancaria

@pytest.fixture
def banco():
    banco = Banco()
    banco.adicionar_conta("João",1000)
    banco.adicionar_conta("Maria",500)
    return banco


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

