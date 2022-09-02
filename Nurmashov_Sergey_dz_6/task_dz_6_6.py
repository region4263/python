# Задать список из N элементов, заполненных числами из [-N, N]. Найти
# произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

import random

# генерируем список из N элементов из промежутка [-N, N]
N = int(input('введи число: '))
lis = [random.randint(-N, N) for _ in range(N)]
print(lis)

with open('file.txt', 'r', encoding='utf-8') as f:
    # в файле прописаны позиции 1, 2, 3
    total = [1]
    [total.append(total[-1] * lis[int(i)]) for i in f]
    print(total[-1])
