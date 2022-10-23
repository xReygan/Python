# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random
k = int(input('Введите натуральную степень: '))
series = []
polynom = list("")
for i in range(k + 1):
    series.append(random.randint(0, 100))
print(series)

for i in range(k + 1):
    if series[i] == 0:
        continue
    else:
        if abs(i - k) == 1:
            polynom.append(str(series[i]) + 'x')
        else:
            polynom.append(str(series[i]) + 'x^' + str(abs(i - k)))
pol = ' ' + ' + '.join(list(polynom)) + ' = 0'
pol_out = ((pol.replace("x^0", "")).replace(" 1x", " x")).lstrip()
print(pol_out)
with open('polynom1.txt', 'w') as data:
    data.write(pol_out)
 
