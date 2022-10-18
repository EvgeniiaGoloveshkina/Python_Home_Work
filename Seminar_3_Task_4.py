#  4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  *Пример:*
#  - 45 -> 101101
#  - 3 -> 11
#  - 2 -> 10


number = int(input("Введите десятичное число:"))

output = []

while number > 0:
    output.insert(0, number % 2)
    number //= 2

binary = "".join(map(str, output))
print(f"Двоичная запись числа: {binary}")