# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28
# конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько
# конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

import random


# проверяем, что введёное число является числом
def digit(a_num):
    while not a_num.isdigit():
        a_num = input('Не корректный ввод. Введи число!: ')
    a_num = int(a_num)
    return a_num


# проверяем соотношение остатка конфет и введённого числа игроком
def true_num(num, sweet):
    num = digit(num)
    if sweet >= 28:
        while num > 28 or num <= 0:
            num = input('Введи число от 1 до 28: ')
            num = digit(num)
    else:
        while num > sweet or num <= 0:
            num = input(f'Введи число от 1 до {sweet}: ')
            num = digit(num)
    return num


# чей ход в игре (игрок №1 или игрок №2)
def player_change(flag_player):
    if flag_player == 1:
        flag_player += 1
    else:
        flag_player -= 1
    return flag_player


# рандомно определяем кто ходит первым
def player_start():
    pl_1_2 = random.randint(1, 2)
    print(f'Жеребьёвка определила, что начинает первым игрок №{pl_1_2}')
    pl_1_2 = player_change(pl_1_2)
    return pl_1_2


# интеллект бота
def computer(main_sw):
    if 144 >= main_sw >= 117:
        comp_num = main_sw - 58
        main_sw -= comp_num
        print(f'Бот походил - {comp_num}. Осталось - {main_sw}')
    elif 115 >= main_sw >= 88:
        comp_num = main_sw - 58
        main_sw -= comp_num
        print(f'Бот походил - {comp_num}. Осталось - {main_sw}')
    elif 86 >= main_sw >= 59:
        comp_num = main_sw - 58
        main_sw -= comp_num
        print(f'Бот походил - {comp_num}. Осталось - {main_sw}')
    elif 57 >= main_sweet >= 30:
        comp_num = main_sw - 29
        main_sw -= comp_num
        print(f'Бот походил - {comp_num}. Осталось - {main_sw}')
    elif 28 >= main_sw >= 1:
        comp_num = main_sw
        main_sw -= comp_num
        print(f'Бот походил - {comp_num}. Осталось - {main_sw}. ПОБЕДА БОТА!!!')
    else:
        comp_num = random.randint(1, 28)
        main_sw -= comp_num
        print(f'Бот походил - {comp_num}. Осталось - {main_sw}')
    return main_sw


# продолжаем игру или конец
def end():
    flag_end = input('Хотите поиграть ещё?\nДА - нажмите 1, НЕТ - любая кнопка: ')
    if flag_end == '1':
        print('ПРОДОЛЖАЕМ!')
        return flag_end, 2021  # 2021 это main_sweet
    print('GAME OVER! Приходите к нам ещё!))')
    return 0, 0


main_sweet = 2021  # конфеты
print('Режимы игры:\n1. Игрок VS Игрок\n2. Игрок VS Компьтер')
game = 0
while not(game == 1 or game == 2):
    game = digit(input('Выберите режим (нажмите 1 или 2): '))
print(f'Всего имеется конфет: {main_sweet}\nНеобходимо вводить число от 1 до 28')
flag = 1
if game == 1:
    player = player_start()
    while main_sweet and flag:
        player = player_change(player)
        main_sweet -= true_num(input(f'Ход игрока №{player}: '), main_sweet)
        print(f'Осталось конфет: {main_sweet}')
        if main_sweet == 0:
            print(f'ПОБЕДА! Выиграл игрок №{player}')
            flag, main_sweet = end()
            if main_sweet and flag:
                player = player_start()
else:
    while main_sweet and flag:
        main_sweet -= true_num(input(f'Ход игрока: '), main_sweet)
        print(f'Осталось конфет: {main_sweet}')
        if main_sweet:
            main_sweet = computer(main_sweet)
            if main_sweet == 0:
                flag, main_sweet = end()
        else:
            print(f'Игрок походил. Осталось - {main_sweet}. ПОБЕДА ИГРОКА!!!')
            flag, main_sweet = end()
