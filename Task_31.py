# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите натуральное число N: "))
simple_multipliers = []
for i in range(number - 1, 1, -1):
    simple = 0
    if (number % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                simple = simple + 1
        if (simple == 0):
            simple_multipliers.append(i)

print(f"Простые множители числа {number}: {simple_multipliers}")
