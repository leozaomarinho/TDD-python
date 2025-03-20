import pytest
from src.models import Banco,ContaBancaria

@pytest.fixture
def banco():
    banco = Banco()
    banco.adicionar_conta("João",1000)
    banco.adicionar_conta("Maria",500)
    return banco

