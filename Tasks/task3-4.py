# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# 45 -> 101101
# 3 -> 11
# 2 -> 10

dex = input('Введите десятичное число: ')
temp = int(dex)
bin = ''
while temp > 0:
    x = int(temp % 2)
    temp = int(temp / 2)
    bin = str(str(x) + bin)
print(dex, '(dex)', end=' --> ')
print(bin, '(bin)')
