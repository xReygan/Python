# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число N: '))
print('N =', n, end=' --> ')
series = []
sum = 0
for i in range(n):
    series.append((1 + 1 / (i + 1)) ** (i + 1))
    sum = sum + series[i]
print(sum, end=' ')
