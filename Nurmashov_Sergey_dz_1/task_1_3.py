# проверяем, чтобы число не было равно 0
def not_null(num):
    if num == 0:
        while num == 0:
            num = int(input('введи число, не равное нулю - '))
        return num
    else:
        return num


x = not_null(int(input('введите координату Х = ')))
y = not_null(int(input('введите координату Y = ')))

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')
