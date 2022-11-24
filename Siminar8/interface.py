import controller

global ide, name, birthday, department, speciality, telephone, receipt, c, r

def start_input():
    menu = '''        1 - Генерировать таблицу персонала компании
        2 - Сохранить таблицу персонала компании (save)
        3 - Загрузить таблицу персонала компании (load)
        4 - Просмотреть таблицу персонала компании
        5 - Редактировать таблицу персонала компании
            (новая запись, исправление, удаление)
        6 - Выход
    --> '''
    c = int(input(menu))
    return c


def start2_input():
    r = int(input('1 - новая запись, 2 - исправление, 3 - удаление: --> '))
    return r


def add_input():
    new_name = input('Введите Ф.И.О. сотрудника : ')
    new_birthday = input('Введите год рождения сотрудника: ')
    new_department = input('Введите отдел работы сотрудника: ')
    new_speciality = input('Введите должность сотрудника: ')
    new_telephone = input('Введите телефон сотрудника: ')
    new_receipt = input('Введите дату приема на работу сотрудника: ')
    return new_name, new_birthday, new_department, new_speciality, new_telephone, new_receipt


def edit_input(name, birthday, department, speciality, telephone, receipt):
    r_ide = int(input('Введите id для исправления: '))
    print(name[r_ide])
    r_name = input(' --> Новое имя: ')
    print(birthday[r_ide])
    r_birthday = input(' --> Новый день рождения: ')
    print(department[r_ide])
    r_department = input(' --> Новый отдел работы: ')
    print(speciality[r_ide])
    r_speciality = input(' --> Новая должность работы: ')
    print(telephone[r_ide])
    r_telephone = input(' --> Новый телефон: ')
    print(receipt[r_ide])
    r_receipt = input(' --> Новая дата приема: ')
    return r_ide, r_name, r_birthday, r_department, r_speciality, r_telephone, r_receipt


def del_input():
    d_ide = int(input('Введите id для удаления: '))
    return d_ide


def viewer(ide, name, birthday, department, speciality, telephone, receipt):
    if len(ide) <= 1: print('Внимание!!! В таблице нет данных!!!')
    print('-'*120)
    print('{:^3} {:^35} {:^12} {:^20} {:^20} {:^12} {:^12}'.format(ide[0], name[0], birthday[0], department[0], speciality[0], telephone[0], receipt[0]))
    for i in range(1, len(ide)):
        if i == 1 or (i - 1) % 3 == 0: print('-'*3, '-'*35, '-'*12, '-'*20, '-'*20, '-'*12, '-'*12)
        print('{:^4} {:<35} {:<12} {:<20} {:<20} {:<12} {:<12}'.format(ide[i], name[i], birthday[i], department[i], speciality[i], telephone[i], receipt[i]))
    print('-'*120)
