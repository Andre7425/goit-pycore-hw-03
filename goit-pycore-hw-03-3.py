import re

def normalize_phone(phone_number):
  """
  Нормалізує телефонний номер до стандартного формату +380...

  Args:
    phone_number: Рядок з телефонним номером у будь-якому форматі.

  Returns:
    Нормалізований номер телефону у вигляді рядка.
  """
  # Крок 1: Видаляємо всі символи, крім цифр та '+'
  cleaned_number = re.sub(r'[^\d+]', '', phone_number)

  # Крок 2: Перевіряємо та стандартизуємо префікс
  if cleaned_number.startswith('+380'):
    return cleaned_number
  elif cleaned_number.startswith('380'):
    return '+' + cleaned_number
  else:
    # Для номерів типу '0501234567'
    return '+38' + cleaned_number

# --- Приклад використання ---
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", sanitized_numbers)