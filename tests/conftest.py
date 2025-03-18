import pytest
from src.models import ContaBancaria

@pytest.fixture
def conta():
    return ContaBancaria("João", 100)
#utilizando o fixture para nao repetir o codigo em todos os testes

