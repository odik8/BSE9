#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

def get_birthdate():
    while True:
        try:
            date_str = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
            birthdate = datetime.strptime(date_str, "%d.%m.%Y").date()
            return birthdate
        except ValueError:
            print("Ошибка! Неправильный формат даты. Попробуйте снова.")

def add_contact(contacts):
    print("\nДобавление нового контакта:")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    birthdate = get_birthdate()

    contact = {
        'фамилия': last_name,
        'имя': first_name,
        'номер телефона': phone_number,
        'дата рождения': birthdate
    }

    contacts.append(contact)
    contacts.sort(key=lambda x: x['дата рождения'])
    print("Контакт успешно добавлен!\n")

def find_contact_by_phone(contacts, phone):
    for contact in contacts:
        if contact['номер телефона'] == phone:
            return contact
    return None

def print_contact(contact):
    if contact:
        print("\nИнформация о человеке:")
        print(f"Фамилия: {contact['фамилия']}")
        print(f"Имя: {contact['имя']}")
        print(f"Номер телефона: {contact['номер телефона']}")
        print(f"Дата рождения: {contact['дата рождения'].strftime('%d.%m.%Y')}\n")
    else:
        print("Контакт не найден.\n")

def main():
    contacts = []

    while True:
        print("1. Добавить контакт")
        print("2. Найти контакт по номеру телефона")
        print("3. Вывести список контактов")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            phone_to_find = input("Введите номер телефона для поиска: ")
            found_contact = find_contact_by_phone(contacts, phone_to_find)
            print_contact(found_contact)
        elif choice == '3':
            for _ in contacts: print_contact(_)
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
