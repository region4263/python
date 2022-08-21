import random

# создаём список
list_1 = []
n = int(input('введи число (количество элементов в списке): '))
for _ in range(n):
    x = random.randint(1, 9)
    list_1.append(x)
print(list_1)

total = 0
for i in range(len(list_1)):
    if i % 2 != 0:
        total += list_1[i]
print(total)
