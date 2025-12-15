import unittest
from logic import calculate_pyramidal_sum

class TestBlackBox(unittest.TestCase):

    def test_valid_positive_class(self):
        """Клас валідних натуральних чисел (n > 0)."""
        # n=3 -> Pn=10. Це представник "хороших" даних.
        result = calculate_pyramidal_sum(3)
        self.assertEqual(result, 10)
        
        # Перевіряємо тип результату (assertIsInstance з твоїх скріншотів)
        self.assertIsInstance(result, int)

    def test_invalid_negative_class(self):
        """Клас невалідних від'ємних чисел (n < 0)."""
        with self.assertRaises(ValueError):
            calculate_pyramidal_sum(-5)

    def test_invalid_type_class(self):
        """Клас невалідних типів даних string."""
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum("five")

    def test_float_number(self):
        """Чи спрацює код, якщо передати 5.0 (float)?"""
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(5.0)

    def test_none_input(self):
        """Що буде, якщо передати None?"""
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(None)

    def test_large_number(self):
        """Перевірка на переповнення або дуже великі числа."""
        n = 1000
        result = calculate_pyramidal_sum(n)
        
        self.assertGreater(result, n)
        self.assertTrue(result > 0)
class TestWhiteBox(unittest.TestCase):

    def test_path_type_error(self):
        """
        Start -> Check Type (Fail) -> Raise TypeError -> End
        """
        # Вхідні дані підібрані так, щоб умова 'if not isinstance' стала True
        input_data = "hello" 
        
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(input_data)

    def test_path_value_error(self):
        """
        Start -> Check Type (Pass) -> Check Value < 0 (Fail) -> Raise ValueError -> End
        """
        # Вхідні дані: int (проходить 1-й if), але < 0 (заходить в 2-й if)
        input_data = -5
        
        with self.assertRaises(ValueError):
            calculate_pyramidal_sum(input_data)

    def test_path_success_calculation(self):
        """
        White Box Path 3:
        Start -> Check Type (Pass) -> Check Value < 0 (Pass) -> Calculate -> Return
        """
        # Вхідні дані: int і >= 0. Проходить повз усі if прямо до формули.
        input_data = 3
        expected_result = 10
        
        result = calculate_pyramidal_sum(input_data)
        self.assertEqual(result, expected_result)

    def test_formula_operators(self):
        """
        Перевіряємо, чи правильно працює формула (n*(n+1)*(n+2)) // 6
        Особливо нас цікавить цілочисельне ділення.
        """
        # Для n=4: 4 * 5 * 6 = 120. 120 / 6 = 20.
        # Якби там було звичайне ділення /, результат був би 20.0 (float),
        # а ми очікуємо int. Це тест на структуру даних.
        result = calculate_pyramidal_sum(4)
        
        # Перевірка саме типу (що ми використали //, а не /)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()