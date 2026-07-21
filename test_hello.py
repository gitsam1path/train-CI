"""Petit module de démonstration avec des fonctions mathématiques."""

from hello import add, multiply


def test_add():
    assert add(2, 3) == 5

def test_add_negatives():
    assert add(-1, -4) == -5

def test_multiply():
    assert multiply(3, 4) == 12
