import unittest
from resta import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-1, 1), -2)
        # Ceros
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(5, 0), 5)
        self.assertEqual(restar(0, 5), -5)
        # Valores límite
        self.assertEqual(restar(1, 10**2), -999999)
        self.assertEqual(restar(-10**2, -1), -999999)

if __name__ == '__main__':
    unittest.main()