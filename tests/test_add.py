import pytest
from add import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -4) == -5


def test_add_zero():
    assert add(0, 0) == 0


@pytest.mark.parametrize("a,b,expected", [(1, 1, 2), (10, -5, 5), (2.5, 2.5, 5.0)])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
