import pytest


@pytest.mark.parametrize("num, result", [(1,11), (2,22), (3,33), (4,44)])
def test_calculation(num, result):
    assert 11*num == result
