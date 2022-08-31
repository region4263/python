# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:
# 12W1B12W3B24W1B14W


st = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
total = list()
t = list(st[0])
count = 1
for i in st[1:]:
    if i == t[-1]:
        count += 1
        t.append(i)
    else:
        total.append(str(count) + t[-1])
        t.append(i)
        count = 1

total.append(str(count) + t[-1])
total = ''.join(total)
print(total)
