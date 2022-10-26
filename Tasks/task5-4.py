# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_in.txt', 'r') as data:
    vx = data.read()
print(vx)
cod = ''
n = 1
for i in range(len(vx) - 1):
    if vx[i] == vx[i + 1] and n != 27:
         n = n + 1
    else:
        if n == 10: n = 'A'
        elif n == 11: n = 'a'
        elif n == 12: n = 'B'
        elif n == 13: n = 'b'
        elif n == 14: n = 'C'
        elif n == 15: n = 'c'
        elif n == 16: n = 'D'
        elif n == 17: n = 'd'
        elif n == 18: n = 'E'
        elif n == 19: n = 'e'
        elif n == 20: n = 'F'
        elif n == 21: n = 'f'
        elif n == 22: n = 'G'
        elif n == 23: n = 'g'
        elif n == 24: n = 'H'
        elif n == 25: n = 'h'
        elif n == 26: n = 'I'
        elif n == 27: n = 'i'
        cod = cod + str(n) + vx[i]
        n = 1
cod = cod + str(n) + vx[len(vx) - 1]
print(cod)
with open('file_out.txt', 'w') as data:
    data.write(cod)


with open('file_out.txt', 'r') as data:
    cod = data.read()
decod = ''
for i in range(0, len(cod) - 1, 2):
    if cod[i] < 'A': n = int(cod[i])
    elif cod[i] == 'A': n = 10
    elif cod[i] == 'a': n = 11
    elif cod[i] == 'B': n = 12
    elif cod[i] == 'b': n = 13
    elif cod[i] == 'C': n = 14
    elif cod[i] == 'c': n = 15
    elif cod[i] == 'D': n = 16
    elif cod[i] == 'd': n = 17
    elif cod[i] == 'E': n = 18
    elif cod[i] == 'e': n = 19
    elif cod[i] == 'F': n = 20
    elif cod[i] == 'f': n = 21
    elif cod[i] == 'G': n = 22
    elif cod[i] == 'g': n = 23
    elif cod[i] == 'H': n = 24
    elif cod[i] == 'h': n = 25
    elif cod[i] == 'I': n = 26
    elif cod[i] == 'i': n = 27
    decod = decod + cod[i + 1] * n
print(decod)
with open('file_dein.txt', 'w') as data:
    data.write(decod)
    