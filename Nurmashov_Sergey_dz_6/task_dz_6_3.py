# Подсчитать сумму цифр в вещественном числе.

num = 46.37

# вариант № 1
ls = [i for i in str(num) if i.isdigit()]
result = sum(list(map(lambda x: int(x), ls)))
print(result)

# вариант № 2
ls = [int(i) for i in str(num) if i.isdigit()]
result = sum(ls)
print(result)
