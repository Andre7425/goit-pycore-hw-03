# функція
import random

def get_numbers_ticket(min_val, max_val, quantity):
  """
  Генерує набір унікальних випадкових чисел для лотерейного квитка.

  Args:
    min_val: Мінімальне можливе число (не менше 1).
    max_val: Максимальне можливе число (не більше 1000).
    quantity: Кількість чисел для вибору.

  Returns:
    Відсортований список унікальних випадкових чисел або порожній список,
    якщо параметри невалідні.
  """
  # Крок 1: Валідація вхідних даних
  if not (1 <= min_val <= max_val <= 1000 and quantity <= (max_val - min_val + 1)):
    return []

  # Крок 2: Генерація унікальних чисел
  random_numbers = random.sample(range(min_val, max_val + 1), quantity)

  # Крок 3: Сортування та повернення результату
  return sorted(random_numbers)

# --- Приклад використання ---
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

another_ticket = get_numbers_ticket(1, 36, 5)
print("Інший квиток:", another_ticket)

invalid_ticket = get_numbers_ticket(50, 1, 5)
print("Невалідний квиток:", invalid_ticket)