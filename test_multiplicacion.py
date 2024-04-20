import unittest
from multiplicacion import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(-1, 1), -1)
        # Ceros
        self.assertEqual(multiplicar(0, 0), 0)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(0, 5), 0)
        # Valores límite
        self.assertEqual(multiplicar(1, 10**6), 10**2)
        self.assertEqual(multiplicar(-1, 10**6), -10**2)

if __name__ == '__main__':
    unittest.main()