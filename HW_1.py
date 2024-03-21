def total_salary(path):
    total_salary = 0  # Ініціалізація загальної суми заробітної плати
    num_developers = 0  # Ініціалізація кількості розробників
    try:
        with open(path, 'r', encoding='utf-8') as file:  # Відкриття файлу для читання
            for line in file:  # Ітерація по кожному рядку у файлі
                developer, salary = line.strip().split(',')  # Розділення рядка на розробника та зарплату
                total_salary += int(salary)  # Додавання зарплати до загальної суми
                num_developers += 1  # Збільшення кількості розробників на 1
    except FileNotFoundError:  # Обробка винятку, якщо файл не знайдено
        print("Файл не знайдено")  # Виведення повідомлення про помилку
    except ValueError:  # Обробка винятку, якщо виникає помилка перетворення типів
        print("Файл пошкодженний")  # Виведення повідомлення про помилку
        return None  # Повернення None у випадку помилки
    if num_developers == 0:  # Перевірка, чи файл пустий
        print("Файл пустий")  # Виведення повідомлення про порожній файл
        return None  # Повернення None у випадку порожнього файлу
    else:
        average_salary = total_salary / num_developers  # Обчислення середньої заробітної плати
    return total_salary, average_salary  # Повернення загальної суми та середньої заробітної плати

# Виклик функції та виведення результатів
total, average = total_salary("path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
