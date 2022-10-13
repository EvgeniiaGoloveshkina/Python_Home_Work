# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def composition(n, res):
    if n == 1:
        res.append(1)
        return n
    else:
        elements = n * composition(n - 1, res)
        res.append(elements)
        return elements

n = int(input('Введите число N: '))
if n > 0:
    res = []
    elements = composition(n, res)
    print(f"Произведение чисел от 1 до N:  {res}")
else:
    print('Введены не корректные данные')