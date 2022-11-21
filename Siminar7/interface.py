import controller

global ide
global name
global birthday
global work
global telephone

def start_input():
    print('1 - Генерировать справочник')
    print('2 - Сохранить справочник')
    print('3 - Загрузить справочник')
    print('4 - Просмотреть справочник')
    print('5 - Редактировать справочник')
    print('6 - Выход')
    c = int(input('--> '))
    return c


def start2_input():
    r = int(input('1 - новая запись, 2 - исправление, 3 - удаление: --> '))
    return r


def add_input():
    new_name = input('Введите новое имя: ')
    new_birthday = input('Введите новый день рождения: ')
    new_work = input('Введите новое место работы: ')
    new_telephone = input('Введите новый телефон:')
    return new_name, new_birthday, new_work, new_telephone


def edit_input(name, birthday, work, telephone):
    r_ide = int(input('Введите id для исправления: '))
    print(name[r_ide])
    r_name = input(' --> Новое имя: ')
    print(birthday[r_ide])
    r_birthday = input(' --> Новоый день рождения: ')
    print(work[r_ide])
    r_work = input(' --> Новое место работы: ')
    print(telephone[r_ide])
    r_telephone = input(' --> Новый телефон: ')
    return r_ide, r_name, r_birthday, r_work, r_telephone


def del_input():
    d_ide = int(input('Введите id для удаления: '))
    return d_ide


def viewer(ide, name, birthday, work, telephone):
    if len(ide) < 1: print('Внимание!!! В справочнике данных нет!!!')
    for i in range(len(ide)):
        print('{:^4} {:^32} {:^20} {:^20} {:^20}'.format(ide[i], name[i], birthday[i], work[i], telephone[i]))

