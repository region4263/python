number_day = 0
while number_day < 1 or number_day > 7:
    number_day = int(input('введи число, обозначающее день недели (от 1 до 7) - '))

if number_day < 6:
    print('нет')
else:
    print('да')
