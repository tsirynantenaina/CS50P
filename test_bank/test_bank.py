from bank import value

def test_value_hello():
    assert value("hello world") == 0

def test_value_h():
    assert value("hi there") == 20

def test_value_default():
    assert value("goodbye") == 100
