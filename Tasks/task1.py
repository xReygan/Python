# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
#	6 -> да
#	7 -> да
#	1 -> нет

x = int(input('Введите число, обозначающее день недели: '))
if 1 < x > 7:
    print('Внимание!!! Некорректный ввод!')
    quit()
if  1 <= x <= 5:
    print('Нет')
else:
    print('Да')