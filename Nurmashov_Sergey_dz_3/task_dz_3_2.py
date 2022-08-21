import random

# создаём список
list_1 = []
n = int(input('введи число (количество элементов в списке): '))
for _ in range(n):
    x = random.randint(1, 9)
    list_1.append(x)
print(list_1)

# ищем середину списка
if len(list_1) % 2 == 0:
    n = len(list_1) // 2
else:
    n = len(list_1) // 2 + 1

total = []
for i in range(n):
    elem = list_1[i] * list_1[-(i + 1)]
    total.append(elem)

print(total)
