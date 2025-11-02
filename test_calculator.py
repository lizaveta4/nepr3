import unittest
from calculator import Calculator
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(5, 0)

    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(30), 0.5, places=3)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(60), 0.5, places=3)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            self.calc.sqrt(-9)

    def test_floor(self):
        self.assertEqual(self.calc.floor(4.9), 4)

    def test_ceil(self):
        self.assertEqual(self.calc.ceil(4.1), 5)

    def test_memory_functions(self):
        self.calc.memory_clear()
        self.calc.memory_add(10)
        self.calc.memory_subtract(3)
        self.assertEqual(self.calc.memory_recall(), 7)
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory_recall(), 0)

if __name__ == '__main__':
    unittest.main()
