# Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности, список повторяемых и убрать дубликаты
# из заданной последовательности.

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

subsequence = [1, 2, 3, 5, 1, 5, 3, 10]

unique = []
repeating = []
for i in range (0, len(subsequence)):
    n = 0
    for j in range (0, len(subsequence)):
        if subsequence[i] == subsequence[j] and not(i == j):
            n = n + 1
    if n == 0: unique.append(subsequence[i])
    if n > 0: repeating.append(subsequence[i])
repeating = list(set(repeating))
no_duplicate = list(set(subsequence))

print('Исходная последовательность чисел:', subsequence)
print('Список уникальных элементов из исходной:', unique)
print('Список повторяемых элементов из исходной:', repeating)
print('Список элементов без дубликатов из исходной:', no_duplicate)