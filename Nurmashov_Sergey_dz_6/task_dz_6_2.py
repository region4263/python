# Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('введи число: '))

# вариант № 1
value = [i * 3 + 1 for i in range(1, n + 1)]
key = [i for i in range(1, n + 1)]
dic = dict(zip(key, value))
print(dic)

# вариант № 2
dic = dict((i, i * 3 + 1) for i in range(1, n + 1))
print(dic)
