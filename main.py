contacts = []

while True:
    print("1. Показать контакты")
    print("2. Добавить контакт")
    print("3. Изменить контакт")
    print("4. Удалить контакт")


    choice = input("> ")

    if choice == "1":
        for contact in contacts:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")
    elif choice == "2":
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        contacts.append({"name": name, "phone": phone})
    elif choice == "3":
        name = input("Введите имя контакта для изменения: ")
        new_phone = input("Введите новый телефон: ")
        for contact in contacts:
            if contact['name'] == name:
                contact['phone'] = new_phone
    elif choice == "4":
        name = input("Введите имя контакта для удаления: ")
        contacts = [c for c in contacts if c['name'] != name]