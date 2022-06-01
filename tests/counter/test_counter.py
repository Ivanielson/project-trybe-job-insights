from src.counter import count_ocurrences
from unittest.mock import mock_open, patch


def test_counter():
    file_fake = """
        Uma vez Flamengo, sempre Flamengo
        Flamengo sempre eu hei de ser
        É o meu maior prazer vê-lo brilhar
        Seja na terra, seja no mar
        Vencer, vencer, vencer
        Uma vez Flamengo, Flamengo até morrer
        Na regata ele me mata, me maltrata
        Me arrebata, que emoção no coração
        Consagrado no gramado, sempre amado
        Mais cotado no Fla-Flu, é o ai Jesus
    """
    with patch("builtins.open", mock_open(read_data=file_fake)):
        assert count_ocurrences("dummy", "Flamengo") == 5
        assert count_ocurrences("dummy", "Jesus") == 1
        assert count_ocurrences("dummy", "vencer") == 3
