import unittest
from calculator import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):
    def test_add(self):
        z1 = complex(1, 1)
        z2 = complex(2, 2)
        self.assertEqual(ComplexCalculator.add(z1, z2), complex(3, 3))

    def test_subtract(self):
        z1 = complex(1, 1)
        z2 = complex(2, 2)
        self.assertEqual(ComplexCalculator.subtract(z1, z2), complex(-1, -1))

    def test_multiply(self):
        z1 = complex(1, 1)
        z2 = complex(2, 2)
        # (1+i)(2+2i) = 2 + 2i + 2i - 2 = 4i
        self.assertEqual(ComplexCalculator.multiply(z1, z2), complex(0, 4))

    def test_divide(self):
        z1 = complex(2, 2)
        z2 = complex(2, 0)
        self.assertEqual(ComplexCalculator.divide(z1, z2), complex(1, 1))

    def test_conjugate(self):
        z1 = complex(1, 2)
        self.assertEqual(ComplexCalculator.conjugate(z1), complex(1, -2))

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            ComplexCalculator.divide(complex(1, 1), 0)

if __name__ == '__main__':
    unittest.main()
