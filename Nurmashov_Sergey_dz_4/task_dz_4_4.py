# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.

import random

k = int(input('задайте максимальную степень многочлена (натуральное число): '))

# рандомно создаём степени, которые будут использоваться
st = []
for i in range(k):
    st.append(random.randint(0, k))
st = set(st)  # откидываем повторы, оставляем только уничкальные значения

# формируем многочлен
ls = []
for i in st:
    x = random.randint(0, 100)
    if i == 0:
        ls.append(str(x))
    elif i == 1:
        ls.append(str(x) + '*' + 'x')
    else:
        ls.append(str(x) + '*' + 'x' + '**' + str(i))
ls.reverse()
x = ' + '.join(ls) + ' = 0'

print(x)

with open('total.txt', 'w', encoding='utf-8') as f:
    f.write(x)
