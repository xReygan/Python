# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Добавьте возможность использования скобок,
# меняющих приоритет операций.

# 1+2*3 => 7;
# (1+2)*3 => 9;

def bracket(y):
    s1, s2 = 0, len(y)-1          # индекс открывающейся скобки и индекс закрывающейся скобки
    for i in range(len(y)):       # или края списка
        if y[i] == '(': s1 = i
    for j in range(s1, len(y)):
        if y[j] == ')':
            s2 = j
            break
    return(s1, s2)


x = '5+(12/4-5)*(3.56+4.44-5*5)-5*((32-12)+6/3)/2-5'
#x = '2.55+4.45-6/3*2-4/2/2*3+4'
#x = '((1.55+2.45+6/2)*3-4)/2'
#x = input('Введите выражение: ')
print(x, end = ' = ')
print(eval(x), end = '  <-- Вычисление с помощью функции eval()\n')

x_in = ''
x_in = x.replace("(", " ( ").replace(")", " ) ").replace("+", " + ").replace("-", " + -").replace("*", " * ").replace("/", " / ").split()

while len(x_in) > 1:
    s1, s2 = bracket(x_in)[0], bracket(x_in)[1]
    n = x_in[s1: s2].count('/')
    while n != 0:
        s1, s2 = bracket(x_in)[0], bracket(x_in)[1]
        i = x_in.index('/', s1, s2)
        x_in[i - 1] = float(x_in[i - 1]) / float(x_in[i + 1])
        del x_in[i]
        del x_in[i]
        n = n - 1

    s1, s2 = bracket(x_in)[0], bracket(x_in)[1]
    n = x_in[s1: s2].count('*')
    while n != 0:
        s1, s2 = bracket(x_in)[0], bracket(x_in)[1]
        i = x_in.index('*', s1, s2)
        x_in[i - 1] = float(x_in[i - 1]) * float(x_in[i + 1])
        del x_in[i]
        del x_in[i]
        n = n - 1

    s1, s2 = bracket(x_in)[0], bracket(x_in)[1]
    n = x_in[s1: s2].count('+')
    while n != 0:
        s1, s2 = bracket(x_in)[0], bracket(x_in)[1]
        i = x_in.index('+', s1, s2)
        x_in[i - 1] = float(x_in[i - 1]) + float(x_in[i + 1])
        del x_in[i]
        del x_in[i]
        n = n - 1

    s1, s2 = bracket(x_in)[0], bracket(x_in)[1]     # убираем скобки если они есть
    if x_in[s1: s2].count('(') > 0:
        del x_in[s1]
        del x_in[s2-1]
  
print(x, end = ' = ')
print(x_in[0], end = '  <-- Вычисление с помощью программы\n')
