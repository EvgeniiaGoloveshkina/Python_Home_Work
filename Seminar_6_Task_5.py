#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.



sequence = map(int, input('Введите последовательность чиcел, через пробел:').split())

dict = {}

for s in sequence:
    if s not in dict.keys():
        dict[s] = 1
    else:
        dict[s] += 1

print(f'Последовательность из неповторяющихся элементов исходной последователности',list(filter(lambda i: dict[i] == 1, dict)))