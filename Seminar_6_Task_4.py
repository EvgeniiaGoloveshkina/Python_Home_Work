#Подсчитать сумму цифр в вещественном числе.

import os
os.system('cls')
import random

number = random.uniform (100,2)
print('Вещественное число = ',number)
row = str(float(number)).split('.')
figures = row[0]+row[1]  
print('Сумма цифр числа  =', sum(int(i) for i in str(figures))) 