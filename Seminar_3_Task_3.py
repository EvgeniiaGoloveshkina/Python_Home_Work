# 3. Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

for i in range(int(input('Введите количество элемнтов списка: '))):
    list.append(float(input(f' Введите {i+1}й элемент (число с плавающей точкой) = ')))
    if list[i] < 0: list[i] = -list[i]

def difference(list):
    dif_max_min =[]
    for i in range(len(list)):
        dif_max_min.append(list[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(f' Разница между максимальным и минимальным значением дробной части элементов = ',(round(difference(list),2)))