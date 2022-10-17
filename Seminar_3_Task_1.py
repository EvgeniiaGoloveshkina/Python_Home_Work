# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from operator import length_hint
from random import randint
list = []
col=int(input('Введите количество элементов в списке: '))
for i in range(col):
    list.append(randint (-10,10))
# print(list)
sum = 0
for i in range(len(list)):
    if i %  2 != 0:
        sum = sum + list[i]
print(f'Сумма элементов,стоящих на нечетных позициях списка {list} равна', sum)