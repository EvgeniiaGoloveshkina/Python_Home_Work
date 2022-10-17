# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from operator import length_hint
from random import randint
list = []
col=int(input('Введите количество элементов в списке: '))
for i in range(col):
    list.append(randint (-10,10))
print (f'Список элементов:', (list))

size = len(list)
mult = []
for i in range(size):
    if i < size//2:
        mult.append(int(list[i])*int(list[-i-1]))
print(f'Произведение пар чисел списка:' ,(mult))