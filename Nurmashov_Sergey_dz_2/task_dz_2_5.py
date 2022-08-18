# Реализуйте алгоритм перемешивания списка.


import random

# создаём список автоматически из пяти рандомных чисел
lis = []
for _ in range(5):
    lis.append(random.randint(1, 100))
print(lis)

# вариант использования метода shuffle
random.shuffle(lis)
print(f'{lis} - метод shuffle')

# вариант перемешивания "вручную"
lis_2 = []
index_x = []
while len(lis_2) != 5:
    # генерируем произвольный индекс, по которому будем выбирать число из начального списка
    x = random.randint(0, 4)
    # если индекс ещё не применялся (нет в списке index_x)
    if x not in index_x:
        lis_2.append(lis[x])
        index_x.append(x)
print(f'{lis_2} - метод "вручную"')
