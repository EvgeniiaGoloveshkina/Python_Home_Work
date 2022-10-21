# 33. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
import random

k = int(input('Введите коэффициент к: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))

if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())

if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())

if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())

print(f'{first}{second}{third}')

