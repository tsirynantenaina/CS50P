from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(7)
    assert jar.size == 12
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    try:
        jar.deposit(-1)
    except ValueError:
        assert jar.size == 12

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.withdraw(3)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"
    try:
        jar.withdraw(6)
    except ValueError:
        assert jar.size == 5
