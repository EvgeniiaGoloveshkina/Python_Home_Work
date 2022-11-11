# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

num = input('Введите вещественное число:')
num_lst = list('1234567890')
summa = 0

print(sum(list(map(int, list(filter(lambda s: s in num_lst, num))))))

