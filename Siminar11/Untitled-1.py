# %%
# Даны две функции:
# f(x) = x^3 - 50x и g(x) = -x^4 + 88x^2 - 241
# Требуется:
# 1. Найти координаты точек пересечения
# 2. Построить графики функций в одной системе координат
# 3. Построить график функции пересечения

import sympy
from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot

x, f, g, = symbols('x f g')
f = collect((x ** 3 - 50 * x), x)
g = collect((-1 * x ** 4 + 88 * x ** 2 - 241), x)

# 1.  Координаты точек пересечения

cros_point_x = solve(Eq(f, g), x)    # находим координаты х

# %%
cros_point_y = []                    # находим координаты y
for i in range(len(cros_point_x)):
    cros_point_y.append(f.subs(x, cros_point_x[i]))

# %%
# красиво выводим все координаты х, у
print('Всего  ', len(cros_point_x), ' точки пересечения. Координаты точек следующие:')
for i in range(len(cros_point_x)):
    print('x', i+1, ' = ', sympy.N(cros_point_x[i], 5), '   ', 'y', i+1, ' = ',  sympy.N(cros_point_y[i], 5))

# %%
# 2. Графики функций в одной системе координат

plot((f, (x, -10, 10)), (g, (x, -10, 10)), title='Графики функций f, g')

# %%
# 3. Построить график функции пересечения (график общей функции)

res = Symbol('res')
res = f - g
plot(res, (x, -10, 10), title='График функции пересечения f, g')

# %%
# Для наглядности
plot((f, (x, -10, 10)), (g, (x, -10, 10)), (res, (x, -10, 10)), title='Графики функций f, g, f-g')


