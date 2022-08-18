# Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.


import random

# генерируем список из N элементов из промежутка [-N, N]
N = int(input('enter the number: '))
lis = []
for _ in range(N):
    lis.append(random.randint(-N, N))
print(lis)

total = 1
with open('file.txt', 'r', encoding='utf-8') as f:
    # в файле прописаны позиции 1, 4, 5
    for i in f:
        total *= lis[int(i)]
    print(total)
