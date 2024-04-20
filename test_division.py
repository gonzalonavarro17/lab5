import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-6, 3), -2)
        # Ceros
        self.assertEqual(dividir(0, 5), 0)
        # Valores límite
        self.assertEqual(dividir(10**2, 1), 10**2)
        self.assertEqual(dividir(1, 10**2), 1/10**2)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()