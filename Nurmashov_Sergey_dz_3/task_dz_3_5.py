k = int(input('введи число - '))

ls = [0, 1]
for i in range(2, k + 1):
    number = ls[i - 1] + ls[i - 2]
    ls.append(number)

ls_2 = [0, 1]
for i in range(2, k + 1):
    number = ls_2[i - 2] - ls_2[i - 1]
    ls_2.append(number)

ls_2.reverse()
ls_2.extend(ls[1:])

print(ls_2)
