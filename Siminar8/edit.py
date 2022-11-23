global ide, name, birthday, department, speciality, telephone, receipt

def edit(name, birthday, department, speciality, telephone, receipt, r_ide, r_name, r_birthday, r_department, r_speciality, r_telephone, r_receipt):
    name[r_ide] = r_name
    birthday[r_ide] = r_birthday
    department[r_ide] = r_department
    speciality[r_ide] = r_speciality
    telephone[r_ide] = r_telephone   
    receipt[r_ide] = r_receipt


def add(ide, name, birthday, department, speciality, telephone, receipt, new_name, new_birthday, new_department, new_speciality, new_telephone, new_receipt):
    ide.append(str(len(ide)))
    name.append(new_name)
    birthday.append(new_birthday)
    department.append(new_department)
    speciality.append(new_speciality)
    telephone.append(new_telephone)
    receipt.append(new_receipt)


def delit(ide, name, birthday, department, speciality, telephone, receipt, d_ide):
    del ide[d_ide]
    del name[d_ide]
    del birthday[d_ide]
    del department[d_ide]
    del speciality[d_ide]
    del telephone[d_ide]
    del receipt[d_ide]
    for i in range(d_ide, len(ide)):
        ide[i] = str(int(ide[i]) - 1)
