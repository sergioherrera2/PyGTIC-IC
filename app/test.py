from app import *

def test_suma():
    assert suma(3, 6) == 9

def test_resta():
    assert resta(6, 2) == 4

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12

def test_division():
    assert division(8, 4) == 2