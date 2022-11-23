import os
from datetime import datetime as dt
from time import time

def logger(ide, name, birthday, department, speciality, telephone, receipt, c, r):
    time = dt.now()#.strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a', encoding = 'utf-8') as file:
        file.write('{};код команды - подкоманды;{}-{};длн id;{};длн ФИО;{};длн год рожд;{};длн отд;{};длн должн;{};длн тел;{};длн дата приема;{}\n'
                    .format(time, str(c), str(r), len(ide)-1, len(name)-1, len(birthday)-1, len(department)-1, len(speciality)-1, len(telephone)-1, len(receipt)-1))


def save(ide, name, birthday, department, speciality, telephone, receipt):
    with open('tab.csv', 'w') as file:
        file.write('{}\n'.format(';'.join(ide)))
        file.write('{}\n'.format(';'.join(name)))
        file.write('{}\n'.format(';'.join(birthday)))
        file.write('{}\n'.format(';'.join(department)))
        file.write('{}\n'.format(';'.join(speciality)))
        file.write('{}\n'.format(';'.join(telephone)))
        file.write('{}\n'.format(';'.join(receipt)))


def load():
    try:
        with open('tab.csv', 'r') as data:
            tel = data.read().split('\n')
            ide, name, birthday, department, speciality, telephone, receipt = (tel[i].split(';') for i in range(7))
            #ide, name, birthday, work, telephone = tel[0].split(';'), tel[1].split(';'), tel[2].split(';'), tel[3].split(';'), tel[4].split(';')
            return ide, name, birthday, department, speciality, telephone, receipt
    except FileNotFoundError:
        print('Внимание!!! Нет файла с таблицей!. Создайте таблицу.')
        return ['№'], ['Ф.И.О.'], ['Год рождения'], ['Отдел'], ['Должность'], ['Телефон'], ['Дата приема']
