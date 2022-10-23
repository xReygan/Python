# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

import random
n = int(input('Введите число элементов: '))
series = []
for i in range(n):
    series.append(random.randint(0, 10))
print(series, ' --> ')

res = []
for i in series:
    counter = series.count(i)
    if counter == 1:
        res.append(i)
print(res)
