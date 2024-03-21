# Функція parse_input розбиває введену користувачем строку на команду та аргументи.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Переводимо команду в нижній регістр та видаляємо зайві пробіли
    return cmd, *args

# Функція add_contact додає новий контакт у словник contacts.
def add_contact(args, contacts):
    if len(args)!=2:
        return "Невірна кількість аргументів. Будь ласка, введіть ім'я та номер телефону."
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

# Функція change_contact змінює існуючий контакт за введеними користувачем аргументами.
def change_contact(args, contacts):
    if len(args)!=2:
        return "Невірна кількість аргументів. Будь ласка, введіть ім'я та номер телефону."
    name, phone = args
    if name not in contacts:
        return "Контакт не існує."
    contacts[name] = phone
    return "Контакт успішно оновлено."

# Функція show_contacts відображає номер телефону для введеного імені контакту.
def show_contacts(args, contacts):
    if len(args)!= 1:
        return "Невірна кількість аргументів. Будь ласка, введіть ім'я."
    name = args[0]
    if name not in contacts:
        return "Контакт не існує."
    return contacts[name]

# Функція show_all_contacts відображає всі контакти у словнику contacts.
def show_all_contacts(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Основна функція main() встановлює зв'язок з користувачем та обробляє його введення.
def main():
    contacts = {}
    print("Ласкаво просимо до асистент-боту!")
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["закрити", "вихід"]:
            print("До побачення!")
            break
        elif command == "привіт":
            print("Як я можу допомогти вам?")
        elif command == "додати":
            print(add_contact(args, contacts))
        elif command == "змінити":
            print(change_contact(args, contacts))
        elif command == "показати":
            print(show_contacts(args, contacts))
        elif command == "всі":
            print(show_all_contacts(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
