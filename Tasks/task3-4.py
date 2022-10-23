# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# 45 -> 101101
# 3 -> 11
# 2 -> 10

dex = input('Введите десятичное число: ')
temp = int(dex)
bin = ''
while temp:
    x = temp % 2
    #temp //= 2
    temp >>= 1
    bin = str(x) + bin
print(dex, '(dex)', end=' --> ')
print(bin, '(bin)')
                  