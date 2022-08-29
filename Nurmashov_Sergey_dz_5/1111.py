# import random
#
#
# # def digit(a_num):
# #     while not a_num.isdigit():
# #         a_num = input('Не корректный ввод. Введи число!: ')
# #     a_num = int(a_num)
# #     return a_num
# #
# #
# # game = 0
# x = 30
# print('всего 30')
# # # while game != 1 and game != 2:
# # while not(game == 1 or game == 2):
# #     game = int(input('Выберите режим (нажмите 1 или 2): '))
# #     print(game, type(game))
#
# # if game == 1:
# #     print('1')
# # elif game == 2:
# #     print('2')
#
# while x != 0:
#     f = int(input('Ваш ход: '))
#     x -= f
#     print(f'Осталось {x}')
#     if 24 >= x >= 21:
#         f = x - 20
#         x -= f
#         print(f'Компьютер походил - {f}. Осталось {x}')
#     elif 19 >= x >= 16:
#         f = x - 15
#         x -= f
#         print(f'Компьютер походил - {f}. Осталось {x}')
#     elif 14 >= x >= 11:
#         f = x - 10
#         x -= f
#         print(f'Компьютер походил - {f}. Осталось {x}')
#     elif 9 >= x >= 6:
#         f = x - 5
#         x -= f
#         print(f'Компьютер походил - {f}. Осталось {x}')
#     elif 4 >= x >= 1:
#         f = x
#         x -= f
#         print(f'Компьютер походил - {f}. Осталось {x}.ПОБЕДА!')
#         break
#     else:
#         f = random.randint(1, 4)
#         x -= f
#         print(f'Компьютер походил - {f}. Осталось {x}')



ls = [' ', ' ', 'fg3fg']
num = input('введи номер ячейки: ')
if num == '1':
    # print(ls[2], type(ls[2]))
    # ls[2].replace('3', 'X')
    ls[2] = '00000'


print(ls)
