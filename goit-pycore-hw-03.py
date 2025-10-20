
from datetime import datetime, date

def get_days_from_today(date_string: str):
    """
    Перевіряє рядок з датою, конвертує його та повертає рядок з результатом
    або повідомленням про помилку.
    """
    # Видаляємо зайві пробіли на початку та в кінці рядка
    cleaned_string = date_string.strip()
    
    # Попередня перевірка формату (чи є 4 цифри для року)
    date_parts = cleaned_string.split('-')
    if len(date_parts) != 3 or len(date_parts[0]) != 4:
        return "Помилка: Неправильний формат. Будь ласка, введіть дату як РРРР-ММ-ДД."

    # Основний блок перевірки та обчислення
    try:
        # Конвертуємо рядок у дату
        given_date = datetime.strptime(cleaned_string, "%Y-%m-%d").date()
        
        # Отримуємо поточну дату
        today = date.today()
        
        # Обчислюємо різницю в днях
        difference_in_days = (today - given_date).days
        
        # Повертаємо успішний результат у вигляді рядка
        return f"Кількість днів між датами: {difference_in_days}"
        
    except ValueError:
        # Ця помилка виникне, якщо дата не існує (наприклад, "2023-02-30")
        return "Помилка: Неправильна дата. Перевірте день та місяць."

# --- Як використовувати функцію ---
user_input = input("Введіть дату у форматі РРРР-ММ-ДД: ")
result = get_days_from_today(user_input)
print(result)