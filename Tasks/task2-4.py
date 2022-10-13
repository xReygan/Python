# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы хранятся
# в файле file.txt в одной строке одно число.

import random
n = int(input('Введите число N: '))
print('N =', n, end=' --> ')
series = []
sum = 0
multiply = 1
for i in range(n):
    series.append(random.randint(-n, n))
print(series, end=' ==> ')

path = 'file.txt'
data = open(path, 'r')
for i in data:
    if int(i) <= n - 1:
        multiply = multiply * series[int(i)]
    else:
        sum = sum + 1
data.close()
print(multiply)
if sum > 0:
    print('Внимание!!! ', sum, 'элемент-а(ов) нет в произведении')
