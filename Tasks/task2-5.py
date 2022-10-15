# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите число N: '))
print('N =', n, end=' --> ')
series = []
for i in range(n):
    series.append(i + 1)
print(series, ' ==> ')

for i in range(n):
    x = random.randint(0, n - 1)
    tmp = series[i]
    series[i] = series[x]
    series[x] = tmp
print(series)
