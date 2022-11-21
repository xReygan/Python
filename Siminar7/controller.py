from statistics import mode
from interface import start_input
from interface import start2_input
from interface import add_input
from interface import edit_input
from interface import del_input
from interface import viewer
from generator import get_ide
from generator import get_name
from generator import get_birthday
from generator import get_work
from generator import get_telephone
from generator import gener_collection
from logger import log_collection
from logger import save
from logger import load
from edit import add
from edit import edit
from edit import delit


global ide
global name
global birthday
global work
global telephone

def controller():
    ide, name, birthday, work, telephone, = [], [], [], [], [] 
    #для просмотра пустых списков, до загрузки и генерации

    while 1:
        c = start_input()
        match c:
            case 1:
                ide, name, birthday, work, telephone = gener_collection()
                viewer(ide, name, birthday, work, telephone)
                log_collection(ide, name, birthday, work, telephone)
            
            case 2:
                save(ide, name, birthday, work, telephone)
                viewer(ide, name, birthday, work, telephone)

            case 3:
                ide, name, birthday, work, telephone = load()
                viewer(ide, name, birthday, work, telephone)

            case 4:
                viewer(ide, name, birthday, work, telephone)

            case 5:               
                r = start2_input()
                match r:
                    case 1:
                        new_name, new_birthday, new_work, new_telephone = add_input()
                        add(ide, name, birthday, work, telephone, new_name, new_birthday, new_work, new_telephone)
                        viewer(ide, name, birthday, work, telephone)

                    case 2:
                        r_ide, r_name, r_birthday, r_work, r_telephone = edit_input(name, birthday, work, telephone)
                        edit(name, birthday, work, telephone, r_ide, r_name, r_birthday, r_work, r_telephone)
                        viewer(ide, name, birthday, work, telephone)

                    case 3:
                        delit(ide, name, birthday, work, telephone, del_input())
                        viewer(ide, name, birthday, work, telephone)

            case 6:
                exit()
