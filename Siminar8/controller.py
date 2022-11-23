from interface import start_input, start2_input, add_input,edit_input,del_input, viewer
from generator import gener_collection
from logger import logger, save, load
from edit import add, edit, delit
import sys

global ide, name, birthday, department, speciality, telephone, receipt, c, r

def controller():                          #для просмотра пустых списков, до загрузки и генерации
    ide, name, birthday, department, speciality, telephone, receipt = ['№'], ['Ф.И.О.'], ['Год рождения'], ['Отдел'], ['Должность'], ['Телефон'], ['Дата приема']
    c = 0       # код команды для логирования
    
    while True:
        r = 0   # код подкоманды для логирования
        c = start_input()
        match c:
            case 1:
                ide, name, birthday, department, speciality, telephone, receipt = gener_collection()
                viewer(ide, name, birthday, department, speciality, telephone, receipt)
                logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

            case 2:
                save(ide, name, birthday, department, speciality, telephone, receipt)
                viewer(ide, name, birthday, department, speciality, telephone, receipt)
                logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

            case 3:
                ide, name, birthday, department, speciality, telephone, receipt = load()
                viewer(ide, name, birthday, department, speciality, telephone, receipt)
                logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

            case 4:
                viewer(ide, name, birthday, department, speciality, telephone, receipt)
                logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

            case 5:               
                r = start2_input()
                match r:
                    case 1:
                        new_name, new_birthday, new_department, new_speciality, new_telephone, new_receipt = add_input()
                        add(ide, name, birthday, department, speciality, telephone, receipt, new_name, new_birthday, new_department, new_speciality, new_telephone, new_receipt)
                        viewer(ide, name, birthday, department, speciality, telephone, receipt)
                        logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

                    case 2:
                        r_ide, r_name, r_birthday, r_department, r_speciality, r_telephone, r_receipt = edit_input(name, birthday, department, speciality, telephone, receipt)
                        edit(name, birthday, department, speciality, telephone, receipt, r_ide, r_name, r_birthday, r_department, r_speciality, r_telephone, r_receipt)
                        viewer(ide, name, birthday, department, speciality, telephone, receipt)
                        logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

                    case 3:
                        delit(ide, name, birthday, department, speciality, telephone, receipt, del_input())
                        viewer(ide, name, birthday, department, speciality, telephone, receipt)
                        logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)

            case 6:
                if len(ide) > 1:
                    save(ide, name, birthday, department, speciality, telephone, receipt)
                    logger(ide, name, birthday, department, speciality, telephone, receipt, c, r)
                sys.exit()
