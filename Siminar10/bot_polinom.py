# Прикрутить телеграм бота к задаче по сложению многочленов.
 
import re
from datetime import datetime as dt
import telebot
#from telebot import *

def coefficients(string_polynomial):              # строку преобразуем в список коэффициентов
    string_polynomial = ' ' + string_polynomial
    x = (string_polynomial.replace("x ", "x^1 "))
    x = (x.replace(" x^1", " 1x^1"))
    x = (x.replace(" x^", " 1x^"))
    x = (x.replace("-x", "-1x"))
    x = (x.replace("- ", "+ -"))
    x = x.rstrip(' 0').rstrip(' =').split(' + ')
    if x[-1][-1].isnumeric():
        x[-1] = x[-1] + 'x^0'
    x = ' + '.join(x)
    x = re.findall('.''\d+', x)
    x = ' + '.join(x)
    x = (x.replace("^", ""))
    x = x.split(' + ')
    polynom = []
    k = int(x[1])
    d = (k + 1) * 2
    for i in range(k + 1):
        polynom.append(0)
    for i in range(1, len(x), 2):
        polynom[abs(int(x[i]) - k)] = int(x[i - 1])
    return polynom
 
 
def record(series):                     # список коэффициентов преобразуем в строку
    polynom = list("")
    k = len(series) - 1
    for i in range(k + 1):
        if series[i] == 0:
            continue
        else:
            if abs(i - k) == 1:
                polynom.append(str(series[i]) + 'x')
            else:
                polynom.append(str(series[i]) + 'x^' + str(abs(i - k)))
    pol = ' ' + ' + '.join(list(polynom)) + ' = 0'
    pol_out = ((pol.replace("x^0", "")).replace("1x", "x").replace("+ -", "- ")).lstrip()
    return pol_out
    
 
def sum_polinoms(pol1, pol2):                         # суммируем полиномы
    pol_fist = coefficients(pol1)
    pol_second = coefficients(pol2)
    while len(pol_fist) != len(pol_second):           # выравниваем списки слогаемых
        if len(pol_fist) > len(pol_second):
            pol_second.insert(0, 0)
        elif len(pol_fist) < len(pol_second):
            pol_fist.insert(0, 0)
    sum = list(map(lambda x, y: x + y, pol_second, pol_fist))
    sum_out = record(sum)
    return sum_out

 
bot = telebot.TeleBot('Здесь Токен')
 
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, '''Сумматор двух полиномов:
    Введите два полинома разделенных знаком #
    (Введите "help" для подробной интрукции)''')

@bot.message_handler(content_types=['text'])               # принимаем сообщение от пользователя
def get_text_messages(message):
    if message.text == 'help':
        bot.send_message(message.chat.id, '''help: Это Сумматор двух полиномов:
        Полиномы записываются в виде:
        ax^n +(-) bx^m +(-) ... +(-) x +(-) c = 0, где
        a, b, ... c - обычные числа
        x - "икс" неизвестная переменная,
        ^ - возведение в степень
        n, m, ... - показатель степени над основанием x
        +(-) - знак плюс или минус
        Степень должна уменьшаться слева на права
        Знаки (+ - =) выделяются пробелами, если первое
        число отрицательное - минус слитно с числом.
        Пример: -2x^3 + 7x^2 - x - 3 = 0 # 3x^2 + 3x - 9 = 0 
        Нажмите "start" или введите два полинома''')                 
    else:
        pol1 = message.text.split('#')[0]
        pol2 = message.text.split('#')[1]
        sum = sum_polinoms(pol1, pol2)
        bot.send_message(message.chat.id, pol1 + ' сложить с \n' + pol2 + ' получим:\n' + sum)

    time = dt.now()                                        # логирование
    with open('log.csv', 'a', encoding = 'utf-8') as file:
        file.write('{};Пользователь ;{},{};написал следующее: ;{}\n'
                    .format(time, message.from_user.first_name, message.from_user.id, message.text))

bot.infinity_polling()
