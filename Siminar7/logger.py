from datetime import datetime as dt
from time import time

def id_logger(ide):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};ide;{}\n'
                    .format(time, ide))


def name_logger(name):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};name;{}\n'
                    .format(time, name))


def birthday_logger(birthday):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};birthday;{}\n'
                    .format(time, birthday))  


def work_logger(work):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};work;{}\n'
                    .format(time, work))



def telephone_logger(telephone):
    time = dt.now().strftime('%d/%m/%y %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};telephone;{}\n'
                    .format(time, telephone))


def log_collection(ide, name, birthday, work, telephone):
    return(id_logger(ide), name_logger(name), birthday_logger(birthday), work_logger(work), telephone_logger(telephone))


def save(ide, name, birthday, work, telephone):
    with open('tel.csv', 'w') as file:
        file.write('{}\n'.format(';'.join(ide)))
        file.write('{}\n'.format(';'.join(name)))
        file.write('{}\n'.format(';'.join(birthday)))
        file.write('{}\n'.format(';'.join(work)))
        file.write('{}\n'.format(';'.join(telephone)))


def load():
    with open('tel.csv', 'r') as data:
        tel = data.read().split('\n')
        ide, name, birthday, work, telephone = tel[0].split(';'), tel[1].split(';'), tel[2].split(';'), tel[3].split(';'), tel[4].split(';')
        return ide, name, birthday, work, telephone

