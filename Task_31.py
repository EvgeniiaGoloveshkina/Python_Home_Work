# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input(f"Задайте натуральное число: "))
simple_multipliers = []
i = 2
count = number
while i <= count:
    if count % i == 0:
        simple_multipliers.append(i)
        count //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {number}: {simple_multipliers}")
