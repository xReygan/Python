#Задача 3
#Напишите программу, которая принимает на вход координаты точки (X и Y),
#причем X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
#находится эта точка (или на какой оси она находится).

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Введите X: '))
y = int(input('Введите Y: '))
print ('x = ', x , end = ';   ')
print ('y = ', y , end = '   ')
print ('-->' , end = '   ')
if x == 0 and y == 0 :
    print('Точка находится в центре координат')
if x == 0 and y > 0 :
    print('Точка находится на положительной части оси Y')
if x == 0 and y < 0 :
    print('Точка находится на отрицательной части оси Y')
if x > 0 and y == 0 :
    print('Точка находится на положительной части оси X')
if x < 0 and y == 0 :
    print('Точка находится на отрицательной части оси X')
if x > 0 and y > 0 :
    print('Точка находится в 1 четверти')
if x > 0 and y < 0 :
    print('Точка находится в 4 четверти')
if x < 0 and y > 0 :
    print('Точка находится во 2 четверти')
if x < 0 and y < 0 :
    print('Точка находится в 3 четверти')