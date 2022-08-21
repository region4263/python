number = int(input('введи число - '))

ls = []
while number != 0:
    bi = number % 2
    ls.append(str(bi))
    number //= 2

b = ''.join(ls[::-1])

print(b)
