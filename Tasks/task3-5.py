# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число элементов: '))
fibonacci = []
negafibonacci = []
for i in range(n + 1):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
for i in range(n, 0, -1):
    negafibonacci.append(((-1) ** (i + 1)) * fibonacci[i])
print('Для К = ', n, end = ' --> ')
print(negafibonacci + fibonacci)
