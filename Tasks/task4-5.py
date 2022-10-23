# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re
def coefficients(string_polynomial):                # строку преобразуем в список коэффициентов
    x = (string_polynomial.replace("x ", "x^1 "))
    x = (x.replace(" x^1", " 1x^1"))
    x = (x.replace(" x^", " 1x^"))
    x = x.rstrip(' 0').rstrip(' =').split(' + ')
    if x[-1].isnumeric():
        x[-1] = x[-1] + 'x^0'
    x = ' + '.join(x)
    x = re.findall('\d+', x)
    polynom = []
    k = int(x[1])
    d = (k + 1) * 2
    for i in range(k + 1):
        polynom.append(0)
    for i in range(1, len(x), 2):
        polynom[abs(int(x[i]) - k)] = int(x[i - 1])
    return polynom


def record(series):                     # список коэффициентов преобразуем в строку
    polynom = list("")
    k = len(series) - 1
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
    return pol_out
    

with open('polynom.txt', 'r') as data:            # ввод данных из файлов
    pol = data.read()
with open('polynom1.txt', 'r') as data:
    pol1 = data.read()
print(pol, '  складываеи с ')
print(pol1, '  получаем: ==>')
pol_fist = coefficients(pol)
pol_second = coefficients(pol1)
while len(pol_fist) != len(pol_second):           # выравниваем списки слогаемых
    if len(pol_fist) > len(pol_second):
        pol_second.insert(0, 0)
    elif len(pol_fist) < len(pol_second):
        pol_fist.insert(0, 0)
sum = list(map(lambda x, y: x + y, pol_second, pol_fist))
sum_out = record(sum)
print(sum_out)
with open('summa2pol.txt', 'w') as data:          # запись результата в файл
    data.write(sum_out)
