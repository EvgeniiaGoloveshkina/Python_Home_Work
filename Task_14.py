# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

num = input("Введите число: ")
sum = 0
for i in num:
    if i!=".":
        sum = sum + int(i)
print(f"Сумма цифр числа {num} равна: ", sum)