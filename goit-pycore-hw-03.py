from datetime import datetime, date
# функція обрахунку кількості днів
def get_days_from_today(given_date) -> int:
    date_today = date.today()
    return abs(given_date - date_today).days

date_inp = str(input("Введіть дату у форматі РРРР-ММ-ДД:"))
date_parts = date_inp.split('-') # розбиваємо введену стрічку по символу -
if len(date_parts[0]) != 4:      # перевіряємо першу частину на довжину 4
    # ЯКЩО НІ: одразу виводимо помилку
    print("Неправильний формат дати. Введіть у форматі РРРР-ММ-ДД")
else:
    # ЯКЩО ТАК: виконуємо конвертацію, як і раніше
    try:   # перевіряємо винятки на правильність введення дати
        date_n = datetime.strptime(date_inp, "%Y-%m-%d").date()
        date_cnt = get_days_from_today(date_n)
        print("Кількість днів від поточної до заданої дати:", date_cnt)
    except NameError:
         print("Неправильний формат дати. Введіть у форматі РРРР-ММ-ДД")
    except ValueError:
         print("Неправильний формат дати. Введіть у форматі РРРР-ММ-ДД")
    
      