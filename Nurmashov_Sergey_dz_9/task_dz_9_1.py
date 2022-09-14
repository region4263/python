ls = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]  # показ номеров ячеек
ls_front = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # игровое поле
ls_back = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]  # для вычисления выигрыша
stop = []  # для хранения уже использованных ячеек
x_o, flag = '0', 0
end = 1
count = 0


# проверяем, что введёное число является числом
def digit(a_num):
    while not a_num.isdigit():
        a_num = input('Не корректный ввод. Введи число!: ')
    a_num = int(a_num)
    return a_num


# введёное число соответствует номерам ячеек
def true_num(t_num):
    while t_num not in ['11', '12', '13', '21', '22', '23', '31', '32', '33']:
        t_num = input('Не корректный ввод. Введи верный номер ячейки: ')
    return t_num


# проверка - ячейка уже занята или нет
def stop_list(s_num, stop_ls):
    s_num = true_num(s_num)
    while s_num in stop_ls:
        s_num = true_num(input(f'ячейка {s_num} уже занята, введи '
                               f'новый номер: '))
    stop_ls.append(s_num)
    return s_num, stop_ls


# чередование знаков Х и 0
def x_o_change(simbol):
    if simbol == '0':
        return 'X', 1
    return '0', 0


# проверка на победу
def win():
    if ls_3[0][0] == ls_3[0][1] == ls_3[0][2] or ls_3[1][0] == ls_3[1][1] \
            == ls_3[1][2] or ls_3[2][0] == ls_3[2][1] == ls_3[2][2] or \
            ls_3[0][0] == ls_3[1][0] == ls_3[2][0] or ls_3[0][1] == \
            ls_3[1][1] == ls_3[2][1] or ls_3[0][2] == ls_3[1][2] == \
            ls_3[2][2] or ls_3[0][0] == ls_3[1][1] == ls_3[2][2] or \
            ls_3[2][0] == ls_3[1][1] == ls_3[0][2]:
        print('ПОБЕДА! КОНЕЦ ИГРЫ!')
        return 1


# продолжать или конец
def continue_or_end(list_front, list_back, stop_ls):
    end_game = digit(input('Хотите продолжить?\nДА - 1   НЕТ - 0: '))
    if end_game == 1:
        list_2 = [e.copy() for e in list_front]
        list_3 = [e.copy() for e in list_back]
        stop_ls.clear()
        return list_2, list_3, stop_ls, 1
    else:
        print('КОНЕЦ ИГРЫ!')
        return 0, 0, 0, 0



# копирование исходных списков, чтобы не изменялись оригиналы, а работать с их копиями
ls_2 = [e.copy() for e in ls_front]
ls_3 = [e.copy() for e in ls_back]

while end == 1:
    print('номера ячеек:    игровое поле:')
    print(ls[0], '  '.join(ls_2[0]), sep='       ', end='\n')
    print(ls[1], '  '.join(ls_2[1]), sep='       ', end='\n')
    print(ls[2], '  '.join(ls_2[2]), sep='       ', end='\n')

    if win():
        ls_2, ls_3, stop, end = continue_or_end(ls_front, ls_back, stop)
        if end == 0:
            break
        count = 0
    elif count == 9:
        print('КОНЕЦ ИГРЫ!')
        ls_2, ls_3, stop, end = continue_or_end(ls_front, ls_back, stop)
        if end == 0:
            break
        count = 0

    num, stop = stop_list(input('введи номер ячейки: '), stop)
    count += 1

    x_o, flag = x_o_change(x_o)
    if num[0] == '1':
        ls_2[0][int(num[1]) - 1] = x_o
        ls_3[0][int(num[1]) - 1] = flag
    elif num[0] == '2':
        ls_2[1][int(num[1]) - 1] = x_o
        ls_3[1][int(num[1]) - 1] = flag
    elif num[0] == '3':
        ls_2[2][int(num[1]) - 1] = x_o
        ls_3[2][int(num[1]) - 1] = flag

    for _ in range(30):
        print()
