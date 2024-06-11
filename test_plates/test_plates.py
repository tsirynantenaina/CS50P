from plates import is_valid
import pytest


def test_1():
    assert is_valid("AAA22A") == False

def test_2():
    assert is_valid("CS05") == False


def test_3():
    assert is_valid("PI3.14") == False

def test_4():
    assert is_valid("P") == False

def test_5():
    assert is_valid("12") == False

def test_6():
    assert is_valid("ABCD") == True

if __name__ == "__main__":
    main()
