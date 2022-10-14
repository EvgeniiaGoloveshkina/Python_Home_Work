# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

from operator import length_hint
from random import randint
numbers = []
col=int(input('Введите количество элементов в списке: '))
for i in range(col):
    numbers.append(randint (-10,10))

x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print (f'Список элементов:', (numbers))
print(f'Произведение элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)
    

# n = int(input('Введите число N: '))
# start = 1
# end = n * 2 + 1
# positions = range(start, end + 1)

# position1 = int(input('Введите позицию первого элемента: '))
# position2 = int(input('Введите позицию второго элемента: '))

# if position1 not in positions or position2 not in positions:
#     print('Введенны некорректные данные')
# else:
#     numbers = []
#     for i in range(-n, n + 1):
#         numbers.append(i)
#     print(f"Список элементов {numbers}")
#     print(f"Произведение элементов,находящихся на позициях {position1} и {position2} равна {numbers[position1 - 1] * numbers[position2 - 1]}")