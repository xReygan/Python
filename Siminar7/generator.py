from random import randint

def get_ide():
    id = ['№', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return id


def get_name():
    name = ['Имя', 'Василий Алибабаевич', 'Макар Сильный','Чук Серверный', 'Гек Южный', 'Веня Прытко', 'Семен Кале', 'Броня Потерс', 'Джон Малкович', 'Гай Ричи', 'Брюс Ли']
    return name


def get_birthday():
    birthday = ['День Рождения', '10.05.1985', '23.02.1965','11.10.1990', '07.08.1998', '19.03.2004', '29.12.1987', '13.02.2012', '15.06.1998', '10.10.1910', '30.07.1968']
    return birthday


def get_work():
    work = ['Место Работы', 'Астрахань','Владимир', 'Суздаль', 'Курган', 'Тверь', 'Казань', 'Магадан', 'Канзас Сити', 'Сиетл', 'Нью Йорк']
    return work


def get_telephone():
    telephone = ['Телефон', '89274536776', '89336548989', '89274534455', '89034563488', '89442315665', '89998789192', '89016713243', '13029997433', '16893964040', '14025657490']
    return telephone


def gener_collection():
    return (get_ide(), get_name(), get_birthday(), get_work(), get_telephone())