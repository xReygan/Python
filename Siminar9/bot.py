# Прикрутить бота к задачам с предыдущего семинара: Создать калькулятор для работы
# с рациональными и комплексными числами, организовать меню, добавив в него систему
# логирования.

from datetime import datetime as dt
import telebot
from telebot import types
 
bot = telebot.TeleBot('5895390461:AAHYXeXnTDvuQziEmvhyb6QeVNSF_0yzuEQ')

@bot.message_handler(commands=["start"])                   # стартовое меню
def start(m, res=False):
    bot.send_message(m.chat.id, '''Это Калькулятор. Введите:
    "Число", Знак(^ * / + -), "Число") без пробелов, где
    ^ возведение в степень
    * умножение
    / деление
    + сложение
    - вычитание
    Для комплексных чисел введите:
    "Комплексное число", Знак(* / + -), "Комплексное число" без пробелов, где
    комплексное число имеет вид а+вj (3+5j, 5.65-4.32j ...)''')

@bot.message_handler(content_types=['text'])               # принимаем сообщение от пользователя
def get_text_messages(message):                            # для обычных чисел
                      
    time = dt.now()                                        # логирование
    with open('log.csv', 'a', encoding = 'utf-8') as file:
        file.write('{};Пользователь ;{},{};написал следующее: ;{}\n'
                    .format(time, message.from_user.first_name, message.from_user.id, message.text))

    if len(message.text.split('^')) == 2 and message.text.count('j') == 0:
        x = message.text.split('^')
        res = float(x[0]) ** float(x[1])
    
    elif len(message.text.split('/')) == 2 and message.text.count('j') == 0:
        x = message.text.split('/')
        res = float(x[0]) / float(x[1])
   
    elif len(message.text.split('*')) == 2 and message.text.count('j') == 0:
        x = message.text.split('*')
        res = float(x[0]) * float(x[1])
   
    elif len(message.text.split('+')) == 2 and message.text.count('j') == 0:
        x = message.text.split('+')
        res = float(x[0]) + float(x[1])
   
    elif len(message.text.split('-')) == 2 and message.text.count('j') == 0:
        x = message.text.split('-')
        res = float(x[0]) - float(x[1])
                                                           # для комплексных чисел
    elif len(message.text.replace('j+', 'j + ').split(' + ')) == 2:
        x = message.text.replace('j+', 'j + ').split(' + ')
        res = complex(x[0]) + complex(x[1])

    elif len(message.text.replace('j-', 'j - ').split(' - ')) == 2:
        x = message.text.replace('j-', 'j - ').split(' - ')
        res = complex(x[0]) - complex(x[1])

    elif len(message.text.replace('j*', 'j * ').split(' * ')) == 2:
        x = message.text.replace('j*', 'j * ').split(' * ')
        res = complex(x[0]) * complex(x[1])

    elif len(message.text.replace('j/', 'j / ').split(' / ')) == 2:
        x = message.text.replace('j/', 'j / ').split(' / ')
        res = complex(x[0]) / complex(x[1])

    else: bot.send_message(message.chat.id, message.text + ''' - Внимание!!! Неправильный ввод, введите:
        "Число", Знак(^ * / + -), "Число") без пробелов или
        "Комплексное число", Знак(* / + -), "Комплексное число" без пробелов''')
    
    bot.send_message(message.chat.id, message.text + '=' + str(res))

bot.infinity_polling()
