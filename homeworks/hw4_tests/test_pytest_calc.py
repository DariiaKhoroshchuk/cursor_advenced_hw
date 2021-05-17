import pytest
from homeworks.hw4_tests.hw4_tests_calc import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8
    assert add(-10, 3) == -7
    with pytest.raises(TypeError):
        add('8', 5)
        add(8, '5')


def test_sub():
    assert subtract(4, 2) == 2
    assert subtract(-2, 2) == -4
    assert subtract(-2, -2) == 0
    with pytest.raises(TypeError):
        subtract('8', 5)
        subtract(8, '5')


def test_mul():
    assert multiply(2, 2) == 4
    assert multiply(2, 0) == 0
    assert multiply(-2, -2) == 4
    assert multiply(-2, 2) == -4
    assert multiply('8', 5) == '88888'
    assert multiply(8, '5') == '55555555'
    with pytest.raises(TypeError):
        multiply('5', '8')


def test_div():
    assert divide(10, 5) == 2
    assert divide(10, -5) == -2
    assert divide(-10, -5) == 2
    with pytest.raises(ValueError):
        divide(2, 0)
        divide('2', 0)
    with pytest.raises(TypeError):
        divide('8', 5)
        divide('8', 5)
