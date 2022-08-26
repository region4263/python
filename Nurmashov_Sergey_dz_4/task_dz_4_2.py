# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

N = int(input('введите нарутальное число: '))

# раскладываем число на простые множители
ls = []
for i in range(2, N - 1):
    if N % i == 0:
        while N % i == 0:
            N //= i
            ls.append(i)
if ls:
    print(ls)
else:
    print('число является простым')

# считаем сколько раз встречается каждый простой множитель
dic = {}
for i in ls:
    if i not in dic:
        x = ls.count(i)
        dic[i] = x
for key, val in dic.items():
    print(f'множитель: {key}; встречается раз: {val}')

