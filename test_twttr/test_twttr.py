from twttr import shorten

def test_shorten_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("david") == "dvd"
    assert shorten("javascript") == "jvscrpt"

def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("DAVID") == "DVD"
    assert shorten("JAVASCRIPT") == "JVSCRPT"

def test_shorten_mixed_case():
    assert shorten("Hello") == "Hll"
    assert shorten("David") == "Dvd"
    assert shorten("JavaScript") == "JvScrpt"

def test_shorten_non_alphabetic():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("d@v1d") == "d@v1d"
    assert shorten("j@v@scr1pt") == "j@v@scr1pt"
