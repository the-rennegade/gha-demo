from example import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(5, 7) == 12

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 7) == 3
