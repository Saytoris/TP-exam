import unittest
from logic import calculate_pyramidal_sum

class TestPyramidalSum(unittest.TestCase):
    
    def test_simple_cases(self):
        self.assertEqual(calculate_pyramidal_sum(1), 1)
        self.assertEqual(calculate_pyramidal_sum(2), 4)
        self.assertEqual(calculate_pyramidal_sum(3), 10)

    def test_zero(self):
        # Сума 0 елементів = 0
        self.assertEqual(calculate_pyramidal_sum(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_pyramidal_sum(-5)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum("string")
            
    def test_output_type(self):
        # Перевіряємо, що результат є int (а не float)
        self.assertIsInstance(calculate_pyramidal_sum(5), int)

if __name__ == '__main__':
    unittest.main()