# Создайте программу для игры в "Крестики-нолики" при помощи виртуального окружения и PIP

import sys
from tkinter import *

def new_game():           # реакция на кнопку 'новая игра', первый ход всегда за 'х'
    global x
    x = 'O'               # символ текущего активного игрока, 'х' или 'о'
    for row in range(3):
        for col in range(3):
            m[row][col]['text'] = ' '
            m[row][col]['background'] = 'light gray'
    info.configure(text='Идет игра, ход Х')
    global win
    win = True            # игра продолжается
    global n
    n = 0                 # счетчик хода игры


def click(i, j):          # рекция на клик мышки (последовательность ходов игроков)
    global x
    info.configure(text='Идет игра, ход ' + x)
    if x == 'X':
        x = 'O'
    else:
        x = 'X'
    if win == True and m[i][j]['text'] == ' ':
        m[i][j]['text'] = x
    if m[i][j]['text'] == ' ':
        m[i][j]['text'] = x
    global n
    n += 1
    victory(x)
    if win == False:
        info.configure(text='Победа ' + x)
    elif n == 9:
        info.configure(text='Ничья')


def victory(x):           # проверка условия победы
    global win
    for i in range(3):
        if m[i][0]['text'] == x and m[i][1]['text'] == x and m[i][2]['text'] == x:
            m[i][0]['background'] = m[i][1]['background'] = m[i][2]['background'] = 'pink'
            win = False
        elif m[0][i]['text'] == x and m[1][i]['text'] == x and m[2][i]['text'] == x:
            m[0][i]['background'] = m[1][i]['background'] = m[2][i]['background'] = 'pink'
            win = False
        elif m[0][0]['text'] == x and m[1][1]['text'] == x and m[2][2]['text'] == x:
            m[0][0]['background'] = m[1][1]['background'] = m[2][2]['background'] = 'pink'
            win = False
        elif m[2][0]['text'] == x and m[1][1]['text'] == x and m[0][2]['text'] == x:
            m[2][0]['background'] = m[1][1]['background'] = m[0][2]['background'] = 'pink'
            win = False


window = Tk()             # инициализация GUI библиотеки Tkinter
window.title('Крестик-Нолик')
win = True
m = []
n = 0
x = 'O'
for i in range(3):
    line = []
    for j in range(3):
        button = Button(window, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='light gray',
                        command=lambda row=i, col=j: click(row, col))
        button.grid(row=i, column=j, sticky='nsew')
        line.append(button)
    m.append(line)
new_button = Button(window, text='Новая игра',
                    background='gray94', command=new_game)
new_button.grid(row=4, column=0, columnspan=3, sticky='nsew')
info = Label(window, text='Идет игра, ход Х', font=(
    "Arial Bold", 20), background='light green')
info.grid(row=3, column=0, columnspan=3, sticky='nsew')
window.mainloop()
