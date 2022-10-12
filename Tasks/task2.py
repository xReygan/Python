# Задача 2
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

m = 0, 1
for x in m :
    for y in m :
        for z in m :
          print ('x = ', x , end = '   ')
          print ('y = ', y , end = '   ')
          print ('z = ', z , end = '   ')
          a = not (x and y and z)
          b = not x or not y or not z
          if a == b :
            print ('Верно')
          else : print('Не верно')  
    





