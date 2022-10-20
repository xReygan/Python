# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = input('Введите список чисел через запятую: ')
series = n.split(',')
sum = 0
index = ''
for i in range(0, len(series)):
    series[i] = int(series[i])
    if i % 2 != 0:
        sum = sum + series[i]
        index = index + str(series[i])
print(series, end=' --> ')
print('на нечётных позициях элементы ', end='')
print(' и '.join(list(index)), ', ответ: ', sum)
