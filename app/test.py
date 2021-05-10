from app import *
import unittest

class TestDockerapp(unittest.TestCase):
    def test_suma(self):
        assert suma(3, 6) == 9

    def test_resta(self):
        assert resta(6, 2) == 4

    def test_multiplicacion(self):
        assert multiplicacion(3, 4) == 12

    def test_division(self):
        assert division(8, 4) == 2

if __name__=='__main__':
    unittest.main()