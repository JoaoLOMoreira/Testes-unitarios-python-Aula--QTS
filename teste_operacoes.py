import unittest
from calculadora.operacoes import somar, subtrair, multiplicar, dividir

class TestOperacoes(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 2), 3)
        self.assertEqual(subtrair(0, 3), -3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == "__main__":
    unittest.main()
