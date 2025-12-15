import unittest
from logic import calculate_pyramidal_sum

class TestBlackBoxPyramidal(unittest.TestCase):

    # ==========================================
    # 1. МЕТОДОЛОГІЯ: ЕКВІВАЛЕНТНИЙ ПОДІЛ
    # (Equivalence Partitioning)
    # Ми перевіряємо представників різних класів даних.
    # ==========================================

    def test_valid_positive_class(self):
        """Клас валідних натуральних чисел (n > 0)."""
        # n=3 -> Pn=10. Це представник "хороших" даних.
        result = calculate_pyramidal_sum(3)
        self.assertEqual(result, 10)
        
        # Перевіряємо тип результату (assertIsInstance з твоїх скріншотів)
        self.assertIsInstance(result, int)

    def test_invalid_negative_class(self):
        """Клас невалідних від'ємних чисел (n < 0)."""
        # Будь-яке від'ємне число має викликати помилку.
        # Беремо -5 як типового представника.
        with self.assertRaises(ValueError):
            calculate_pyramidal_sum(-5)

    def test_invalid_type_class(self):
        """Клас невалідних типів даних (не цілі числа)."""
        # Рядок замість числа
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum("ten")

    # ==========================================
    # 2. МЕТОДОЛОГІЯ: АНАЛІЗ ГРАНИЧНИХ ЗНАЧЕНЬ
    # (Boundary Value Analysis - BVA)
    # Ми перевіряємо точки переходу між класами.
    # ==========================================

    def test_boundary_zero(self):
        """Нижня межа допустимих значень (n = 0)."""
        # Це граничне значення: мінімально можливе "правильне" число.
        result = calculate_pyramidal_sum(0)
        self.assertEqual(result, 0)

    def test_boundary_minus_one(self):
        """Значення одразу за нижньою межею (n = -1)."""
        # Це перше "неправильне" число зліва від нуля.
        with self.assertRaises(ValueError):
            calculate_pyramidal_sum(-1)

    def test_boundary_one(self):
        """Значення одразу над нижньою межею (n = 1)."""
        # Найменше натуральне число.
        self.assertEqual(calculate_pyramidal_sum(1), 1)

    # ==========================================
    # 3. МЕТОДОЛОГІЯ: ПЕРЕДБАЧЕННЯ ПОМИЛОК
    # (Error Guessing)
    # Специфічні сценарії, де розробник міг помилитися.
    # ==========================================

    def test_float_number(self):
        """Чи спрацює код, якщо передати 5.0 (float)?"""
        # Навіть якщо 5.0 математично ціле, в Python це інший тип.
        # Функція має бути суворою і відхилити float.
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(5.0)

    def test_none_input(self):
        """Що буде, якщо передати None?"""
        # assertIsNone / assertIsNotNone тут допомагають перевірити логіку,
        # але тут ми чекаємо TypeError, бо None не можна множити.
        with self.assertRaises(TypeError):
            calculate_pyramidal_sum(None)

    def test_large_number(self):
        """Перевірка на переповнення або дуже великі числа."""
        # Python автоматично обробляє великі числа (BigInt), 
        # але тест гарантує, що алгоритм не зависає.
        n = 1000
        result = calculate_pyramidal_sum(n)
        
        # Ми знаємо, що для додатних n результат завжди > n
        # (використовуємо assertGreater з твоїх скріншотів)
        self.assertGreater(result, n)
        self.assertTrue(result > 0)

if __name__ == '__main__':
    unittest.main()