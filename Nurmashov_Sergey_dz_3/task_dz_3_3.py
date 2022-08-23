import random

# создаём список
list_1 = []
n = int(input('введи число (количество элементов в списке): '))
for _ in range(n):
    x = random.randint(100, 999)
    list_1.append(x / 100)
print(list_1)

max_elem = min_elem = int(list_1[0] * 100) - int(list_1[0]) * 100

for i in range(1, len(list_1)):
    elem = int(list_1[i] * 100) - int(list_1[i]) * 100

    if elem > max_elem:
        max_elem = elem
    elif elem < min_elem:
        min_elem = elem

print((max_elem - min_elem) / 100)
