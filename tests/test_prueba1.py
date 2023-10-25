import pytest
from scr.prueba1 import mayor

def test_mayor():
    assert mayor(7 , 2) == 7
    assert mayor(34 , 100) == 100
    assert mayor(-4 , 0) == 0
    assert mayor(25 , 25) == 0
    assert mayor(-9 , -2) == -2
    

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (1, 1, 0),
      (17, 3, 17),
      (100, 298, 298),
      (-15, -1, -1),
      (-3, 8, 8)
    ]
)
def test_mayor_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected
    