# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


N = int(input('введи число: '))
ls = [1]
[ls.append(ls[-1] * (-3)) for _ in range(N - 1)]
num = ', '.join(list(map(lambda x: str(x), ls)))
print(num)
