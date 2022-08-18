# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.


n = int(input('enter the number: '))
lis = []
for i in range(1, n + 1):
    lis.append((1 + 1 / i) ** i)
total = sum(lis)
print(total)
