# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

str_data = 'уекгшнезщкщшку свабо итсьчщы, авбс б фыавч, Арваысб Босн.'
x = str_data.split()
print(x)
res = ''
for i in list(x):
    a = i.replace('а', '@').replace('А', '@').replace('б', '%')
    a = a.replace('Б', '%').replace('в', '&').replace('В', '&')
    if a.count('@') >= 1 and a.count('%') >= 1 and a.count('&') >= 1:
        continue
    else:
        res = res + i + ' '
res = res.rstrip()
print('Начальный текст:')
print(str_data)
print('Результат (без слов в которых есть буквы "А, а, Б, б, В, в"):')
print(res)
