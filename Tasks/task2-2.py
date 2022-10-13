# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def faktor(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def prnt(n):
    p = '1'
    if n == 0:
        return p
    else:
        i = 2
        while i != n + 1:
            p = p + '*' + str(i)
            i = i + 1
    return p


n = int(input('Введите число N: '))
print('N =', n, end=' --> ')
res = []
for i in range(n):
    res.append(i + 1)

for i in range(n):
    res[i] = faktor(res[i])
print(res, sep=',', end=' ')

print('(', end=' ')
for i in range(n):
    print(prnt(i + 1), end='')
    if i < n - 1:
        print(',', end=' ')
print(' )')
