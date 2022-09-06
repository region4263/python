def input_d():
    print('импорт будет осуществляться:\n1. вручную\n2. с файла')
    inp = int(input())
    name = ''
    tel = ''
    wrote = ''
    if inp == 1:  # вручную
        data = input('введите данные: ')
        if data.find(',') == -1:  # на одной строке хранится одна часть записи
            count = 1
            while count != 4:
                if count == 1:
                    print(f'Фамилия - {data}')
                    name = input('введите имя - ')
                    print()
                    count += 1
                elif count == 2:
                    print(f'Фамилия - {data}\nИмя - {name}')
                    tel = input('введите телефон - ')
                    print()
                    count += 1
                elif count == 3:
                    print(f'Фамилия - {data}\nИмя - {name}\nТелефон - {tel}')
                    wrote = input('введите описание - ') + '\n'
                    print()
                    count += 1
            print(f'Фамилия - {data}\nИмя - {name}\nТелефон - {tel}\nОписание - {wrote}')
            data = data + '\n' + name + '\n' + tel + '\n' + wrote + '\n'
            with open('input_data.txt', 'a', encoding='utf-8') as f:
                f.write(data)
        else:  # на одной строке хранятся все записи
            data += ';\n'
            print(f'добавлена запись - {data}')
            with open('input_data_str.txt', 'a', encoding='utf-8') as f:
                f.write(data)

    else:  # с файла
        with open('data_str.txt', 'r', encoding='utf-8') as file:
            for data in file:
                if data.find(',') == -1:
                    print(data.replace('\n', ''))
                    with open('input_data.txt', 'a', encoding='utf-8') as f:
                        f.write(data)
                else:
                    print(data.replace('\n', ';'))
                    data = data.replace('\n', ';\n')
                    with open('input_data_str.txt', 'a', encoding='utf-8') as f:
                        f.write(data)


if __name__ == "__main__":
    input_d()
