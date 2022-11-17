from interface import edit_input
import interface
import controller

global ide
global name
global birthday
global work
global telephone


def edit(name, birthday, work, telephone, r_ide, r_name, r_birthday, r_work, r_telephone):
    name[r_ide] = r_name
    birthday[r_ide] = r_birthday
    work[r_ide] = r_work
    telephone[r_ide] = r_telephone


def add(ide, name, birthday, work, telephone, new_name, new_birthday, new_work, new_telephone):
    ide.append(str(len(ide)))
    name.append(new_name)
    birthday.append(new_birthday)
    work.append(new_work)
    telephone.append(new_telephone)


def delit(ide, name, birthday, work, telephone, d_ide):
    del ide[d_ide]
    del name[d_ide]
    del birthday[d_ide]
    del work[d_ide]
    del telephone[d_ide]
    for i in range(d_ide, len(ide)):
        ide[i] = str(int(ide[i]) - 1)

        