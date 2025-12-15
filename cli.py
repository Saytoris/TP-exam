import sys
# Імпортуємо нову функцію розрахунку
from logic import calculate_pyramidal_sum

def run_console_app():
    print("==========================================")
    print(" ОБЧИСЛЕННЯ N-го ПІРАМІДАЛЬНОГО ЧИСЛА")
    print(" Ряд: 1, 3, 6, 10... (суми трикутних чисел)")
    print(" Введіть 'q' або 'exit' щоб вийти.")
    print("==========================================")

    while True:
        try:
            user_input = input("\nВведіть число n: ").strip()

            # Перевірка на команду виходу
            if user_input.lower() in ['q', 'exit']:
                print("Програма завершена. До побачення!")
                break

            # Конвертація та обчислення
            n = int(user_input)
            result = calculate_pyramidal_sum(n)
            
            print(f"-> {n}-й елемент пірамідального числа: {result}")

        except ValueError:
            # Обробка вводу літер або від'ємних чисел (якщо функція викине ValueError)
            print("ПОМИЛКА: Будь ласка, введіть коректне ціле невід'ємне число.")
        except Exception as e:
            print(f"Непередбачена помилка: {e}")

if __name__ == "__main__":
    run_console_app()