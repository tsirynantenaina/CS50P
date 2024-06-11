from um import count
import pytest

def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("Um") == 1

def test_multiple_ums():
    assert count("um, um...") == 2
    assert count("Um, thanks, um...") == 2

def test_um_in_words():
    assert count("yummy") == 0
    assert count("album") == 0

def test_edge_cases():
    assert count("um um um") == 3
    assert count("Um? Um. um!") == 3
    assert count("UM") == 1
    assert count("um,") == 1
    assert count("Um um, um.") == 3
