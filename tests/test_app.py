from app import multiply, alu

def test_multiply():
    assert multiply(2, 3) == 5

def test_alu():
    assert alu(4, 2) == 2
