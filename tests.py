import unittest
from .functions import calculate_multipliers

class TestCalculator(unittest.TestCase):
    def test_calculate_multipliers(self):
        multipliers = [2, 3, 5, 7]
        expected_result = 210
        result = calculate_multipliers(multipliers)
        self.assertEqual(result, expected_result)

if name == 'main':
    unittest.main()