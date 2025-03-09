from src.services import ServicoConta, BancoDeDados

def test_verificar_saldo(mocker):
    mock_banco = mocker.Mock(spec=BancoDeDados)
    mock_banco.obter_saldo.return_value = 100

    servico = ServicoConta(mock_banco)
    saldo = servico.verificar_saldo("João")

    assert saldo == 100
    mock_banco.obter_saldo.assert_called_once_with("João")