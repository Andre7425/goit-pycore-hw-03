from datetime import date, timedelta

def get_upcoming_birthdays(users):
    """
    Визначає, кого з колег потрібно привітати з днем народження 
    на наступному тижні, з урахуванням вихідних.
    """
    today = date.today()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо рядок з датою у datetime об'єкт
        # Замінюємо крапки на тире для сумісності з fromisoformat
        birthday_str = user["birthday"].replace('.', '-')
        birthday = date.fromisoformat(birthday_str)
        
        # Визначаємо дату дня народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження протягом наступних 7 днів
        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday < 7:
            congratulation_date = birthday_this_year
            
            # Якщо день народження на вихідних, переносимо на понеділок
            if birthday_this_year.weekday() >= 5: # 5 - Субота, 6 - Неділя
                days_to_add = 7 - birthday_this_year.weekday()
                congratulation_date += timedelta(days=days_to_add)
            
            # Додаємо результат до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# --- Приклад використання ---
users = [
    {"name": "Іван Петренко", "birthday": "1985.10.12"}, # Ця субота
    {"name": "Марія Іваненко", "birthday": "1990.10.10"}  # Цей четвер
]

upcoming = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming)
# Поточна дата: 2025.10.09 (Четвер)
# Результат: 
# [
#   {'name': 'Марія Іваненко', 'congratulation_date': '2025.10.10'}, 
#   {'name': 'Іван Петренко', 'congratulation_date': '2025.10.13'}
# ]