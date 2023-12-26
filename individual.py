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
            print("Ошибка Неправильный формат даты. Попробуйте снова.")


def add_person(list_of_people):
    print("\nДобавление нового человека:")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    birthdate = get_birthdate()

    person = {
        'фамилия': last_name,
        'имя': first_name,
        'номер телефона': phone_number,
        'дата рождения': birthdate
    }

    list_of_people.append(person)
    list_of_people.sort(key=lambda x: x['дата рождения'])
    print("Человек добавлен\n")


def find_person_by_phone(list_of_people, phone):
    for person in list_of_people:
        if person['номер телефона'] == phone:
            return person
    return None


def print_person(list_of_people):
    if list_of_people:
        print("\nИнформация о человеке:")
        print(f"Фамилия: {list_of_people['фамилия']}")
        print(f"Имя: {list_of_people['имя']}")
        print(f"Номер телефона: {list_of_people['номер телефона']}")
        print(f"Дата рождения: {list_of_people['дата рождения'].strftime('%d.%m.%Y')}\n")
    else:
        print("Человек не найден.\n")


def main():
    list_of_people = []

    while True:
        print("1. Добавить человека")
        print("2. Найти человека по номеру телефона")
        print("3. Вывести список людей")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            add_person(list_of_people)
        elif choice == '2':
            phone_to_find = input("Введите номер телефона для поиска: ")
            found_person = find_person_by_phone(list_of_people, phone_to_find)
            print_person(found_person)
        elif choice == '3':
            for _ in list_of_people: print_person(_)
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
