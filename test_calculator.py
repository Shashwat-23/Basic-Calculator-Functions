from unittest import TestCase
import calculator

class TestCalculator(TestCase):
    def test_divide_by_zero(self):
        calc = calculator.Calculator()
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_add_numbers(self):
        calc = calculator.Calculator()
        result = calc.add(10, 5)
        self.assertEqual(result, 15)