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


def find_person_by_phone(people, phone):
    for person in people:
        match person['номер телефона']:
            case phone:
                return person
    return None


def print_person_info(list_of_people):
    match list_of_people:
        case []:
            print("Человек не найден.\n")
        case {'фамилия': f, 'имя': i, 'номер телефона': nt, 'дата рождения': dr}:
            print("\nИнформация о человеке:")
            print(f"Фамилия: {f}")
            print(f"Имя: {i}")
            print(f"Номер телефона: {nt}")
            print(f"Дата рождения: {dr.strftime('%d.%m.%Y')}\n")


def main():
    list_of_people = []

    while True:
        print("1. Добавить человека")
        print("2. Найти человека по номеру телефона")
        print("3. Вывести список людей")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3/4): ")

        match choice:
            case '1':
                add_person(list_of_people)
            case '2':
                phone_to_find = input("Введите номер телефона для поиска: ")
                found_person = find_person_by_phone(list_of_people, phone_to_find)
                print_person_info(found_person)
            case '3':
                for _ in list_of_people: print_person_info(_)
            case '4':
                print("Программа завершена.")
                break
            case _:
                print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
