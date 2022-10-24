# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
#  Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 

# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

with open('users.txt', 'w', encoding='Utf-8') as f:

    users = ['Иванов Иван Иванович', 'Петров Петр Петрович', 'Сидоров Иван Сидорович',
              'Васильев Александр Иванович', 'Мошков Илья',  'Сергеевич, Кузьмина Мария Петровна']

    for user in users:
        f.write(user + '\n')

with open('hobby.txt', 'w', encoding='Utf-8') as f:
    hobbies = ['Скалолазание, охота', 'Горные лыжи', 'Фотография',
             'Спортивная ходьба', 'Моделирование', 'Рукоделие, фитнес']

    for hobby in hobbies:
        f.write(hobby + '\n')

users_hobby = {}

with open('users.txt', 'r', encoding='Utf-8') as f1:
    with open('hobby.txt', 'r', encoding='Utf-8') as f2:

        while user:
            user = f1.readline()[:-1]
            hobby = f2.readline()[:-1]
            users_hobby[user] = hobby

            if not user:
                del users_hobby['']

with open('users_hobby.txt', 'w', encoding='Utf-8') as f:
    for key, value in users_hobby.items():
        f.write(f'{key} : {value}' + '\n')
