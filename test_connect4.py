import pytest

def add(a, b):
    return a + b


@pytest.mark.parametrize(
    'number1, number2',
    [
        (1,2),
        (2,5),
        (9,6),
    ]
)
def test_add(number1, number2):
    assert (number1 + number2 == add(number1, number2))
    