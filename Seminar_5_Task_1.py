# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) * Подумайте как наделить бота ""интеллектом""
from random import *
import os

def gamer_gamer():
    col_candies = 202
    max_col = 28
    count = 0
    player_1 = input('\nВведите свое имя: ')
    player_2 = input('\nВведите имя соперника: ')

    x = randint(1, 2)
    if x == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    print(f'Игрок {first} ходит первым !')

    while col_candies > 0:
        if count == 0:
            step = int(input(f'\n {first} = '))
            if step > col_candies or step > max_col:
                step = int(input(f'\n Можно взять только {max_col} конфет {first}, попробуй еще раз: '))
            col_candies = col_candies - step
        if col_candies > 0:
            print(f'\n осталось еще {col_candies}')
            count = 1
        else:
            print('Конфеты закончились')

        if count == 1:
            step = int(input(f'\n {second} '))
            if step > col_candies or step > max_col:
                step = int(input(f'\n Можно взять только {max_col} конфет {second}, попробуй еще раз: '))
            col_candies = col_candies - step
        if col_candies > 0:
            print(f'\n осталось еще {col_candies} конфет')
            count = 0
        else:
            print('Конфеты закончились')

    if count == 1:
        print(f'Победил {second} ')
    if count == 0:
        print(f'Победил {first} ')


gamer_gamer()