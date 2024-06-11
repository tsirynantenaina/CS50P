from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True

def test_invalid_addresses():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("275.3.6.28") == False
    assert validate("cat") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False
    assert validate("1234.1.1.1") == False
    assert validate("-1.1.1.1") == False

def test_edge_cases():
    assert validate("256.256.256.256") == False
    assert validate("255.255.255.256") == False
    assert validate("0.0.0.256") == False
    assert validate("192.168.0.01") == True  # leading zeros are allowed but the value should be within range

