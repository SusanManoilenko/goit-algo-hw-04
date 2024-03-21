def get_cats_info(cats):
    cats_info = []  # Створення порожнього списку для зберігання інформації про кішок
    try:
        with open(path, 'r', encoding='utf-8') as file:  
            for line in file:  # Ітерація по кожному рядку у файлі
                cat_data = line.strip().split(',')  # Розбивка рядка за комами
                cat_info = {  # Створення словника із інформацією про кішку
                    "id": cat_data[0],  # Ідентифікатор кішки
                    "name": cat_data[1],  # Ім'я кішки
                    "age": cat_data[2]  # Вік кішки
                }
                cats_info.append(cat_info)  # Додавання інформації про кішку до списку
    except FileNotFoundError:  # Обробка помилки, якщо файл не знайдено
        print("Файл не найден.")  # Виведення повідомлення про помилку
        return None  # Повернення значення None у випадку, якщо файл не знайдено
    except Exception as e:  # Обробка будь-яких інших винятків
        print(f"Виникла помилка: {e}")  # Виведення повідомлення про помилку
        return None  # Повернення значення None для будь-яких інших винятків
    
    return cats_info  # Повернення списку інформації про кішок

# Приклад використання:
cats_info = get_cats_info("cats.txt")
if cats_info is not None:  # Перевірка, чи не є cats_info значенням None
    for cat in cats_info:  
        print(cat)  # Виведення інформації про кішку
else:
    print("Не вдалося отримати інформацію про кішок.")  # Виведення повідомлення, якщо не вдалося отримати інформацію про кішок
