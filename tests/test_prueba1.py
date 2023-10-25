from scr.prueba1 import mayor

def test_mayor():
    assert mayor(7 , 2) == 7
    assert mayor(34, 100) == 100
    assert mayor(-4, 0) == 0
    assert mayor(25 , 25) == 25
    assert mayor(-9 , -2) == -2
    