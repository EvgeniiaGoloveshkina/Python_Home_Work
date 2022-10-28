# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('Seminar_5_Task_3.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('Seminar_5_Task_3.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()

print(my_text)

def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


text_compression = rle_encode(my_text)

with open('Seminar_5_Compression.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)