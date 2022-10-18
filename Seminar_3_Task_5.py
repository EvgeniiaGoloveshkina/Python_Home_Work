# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи
num = int(input('Введите число: '))
print(num)
negafibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,num):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_neg = negafibonacci[i-2] - negafibonacci[i-1]
    negafibonacci.append(list_neg)

negafibonacci.reverse()
negafibonacci.append(0)

print(f'Cписок чисел Фибоначчи, в том числе для отрицательных индексов для k = {num}: \n {negafibonacci+fibonacci}')