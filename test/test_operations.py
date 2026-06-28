from src.basic_math_operations import add,sub,multiplication

def test_add():
    assert add(2,3) == 5
    assert add(80,6) == 86
    assert add(0,3) == 3

def test_sub():
    assert sub(3,0) == 3
    assert sub(3,-5) == -2

def test_mul():
    assert multiplication(1,2) == 2
    assert multiplication(3,20) == 60
    assert multiplication(-2,-2) == 4