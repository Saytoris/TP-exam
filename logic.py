def calculate_pyramidal_sum(n):
    """
    Обчислює n-й елемент "пірамідального числа" (Тетраедричне число).
    Ряд: 1, 3, 6, 10... (сума трикутних чисел)
    Формула: Pn = (n * (n + 1) * (n + 2)) / 6
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Використовуємо // для цілочисельного ділення
    return (n * (n + 1) * (n + 2)) // 6