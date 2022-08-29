# Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

with open('total_1.txt', 'r', encoding='utf-8') as first, \
        open('total_2.txt', 'r', encoding='utf-8') as second:
    temp_one = first.read().split(' ')
    temp_two = second.read().split(' ')

    # (из первого файла) ключ - степень, значение - коэффициент многочлена
    dic_1 = {}
    for i in temp_one[:-2]:
        if 'x**' in i:
            dic_1[i[-1]] = i[:i.find('*')]
        if i.isdigit():
            dic_1['0'] = i

    # (из второго файла) ключ - степень, значение - коэффициент многочлена
    dic_2 = {}
    for i in temp_two[:-2]:
        if 'x**' in i:
            dic_2[i[-1]] = i[:i.find('*')]
        if i.isdigit():
            dic_2['0'] = i

    # суммируем те значения, где совпадают ключи в обоих словарях
    dic_total = dic_1
    for key, val in dic_2.items():
        if key in dic_1:
            val = str(int(val) + int(dic_1[key]))
            dic_total[key] = val
        else:
            dic_total[key] = val

    # сортируем по ключу (чтобы степени располагались упорядоченно)
    # {'5': '172', '0': '132', '3': '59'} --> [('0', '132'), ('3', '59'), ('5', '172')]
    dic_total = sorted(dic_total.items())

    # формируем результирующий многочлен
    total = []
    for key, val in dic_total:
        if key == '0':
            total.append(val)
        elif key == '1':
            total.append(val + '*' + 'x')
        else:
            total.append(val + '*' + 'x' + '**' + key)
    total.reverse()
    x = ' + '.join(total) + ' = 0'

    print(x)

with open('total_dic.txt', 'w', encoding='utf-8') as f:
    f.write(x)
