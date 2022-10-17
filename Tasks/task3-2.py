# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

n = input('Введите список чисел через запятую: ')
series = n.split(',')
multiply = []
index = ''
d = len(series)
for i in range(0, d):
    series[i] = int(series[i])
dim = int(d / 2)
print(series, end=' --> ')
if d % 2 != 0:
    dim = int(d / 2 + 1)
for i in range(0, dim):
    multiply.append(series[i] * series[d - i - 1])
print(multiply)
