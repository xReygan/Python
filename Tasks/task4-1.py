# Вычислить число c заданной точностью d

# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

import math
d = float(input('Введите заданную точность (например: d=0.001): '))
if d > 0.1:
    d = 0.1
elif d < 0.0000000001:
    d = 0.0000000001
num = float(input('Введите число (если хотите Пи, то введите 1; если е, то введите 2): '))
if num == 1:
    num = math.pi
elif num == 2:
    num = math.e
accuracy = int(math.log10(1 / d))
print(f'{num} округляем с точностью до {accuracy} знака после запятой: -->')
print(round(num, accuracy))