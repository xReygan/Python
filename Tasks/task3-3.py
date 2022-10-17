# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

import random
n = int(input('Введите число элементов: '))
series = []
for i in range(n):
    series.append(random.randint(0, 10000) / 100)

fraction = []
for i in series:
    fraction.append(round(i % 1, 2))
difference = max(fraction) - min(fraction)
print(series, end = ' --> ')
print(round(difference, 2))
