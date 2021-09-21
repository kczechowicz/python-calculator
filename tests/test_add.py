from pythoncalculator import add
from pythoncalculator import subtract


def test_subtract():
    assert subtract(1, 3) == -2


def test_add():
    assert add(1, 3) == 4

