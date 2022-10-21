# 32. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
list = [random.randint(1,10) for i in range (10)]
print(f'Последовательность чисел: {list}')
new_list =[]
[new_list.append(i) for i in list if i not in new_list ]
print(f'Cписок неповторяющихся элементов  последовательности: {new_list}')

