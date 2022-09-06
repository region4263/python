def input_one_str():
    """ на одной строке хранится одна часть записи """

    sec_name, name, telefone, wrote = data()
    res_data = sec_name + '\n' + name + '\n' + telefone + '\n' + wrote + '\n' + '\n'
    with open('input_data.txt', 'a', encoding='utf-8') as f:
        f.write(res_data)
        print(f'добавлена запись:\n{res_data}')


def input_all_str():
    """ на одной строке хранятся все записи """

    sec_name, name, telefone, wrote = data()
    res_data = sec_name + ',' + name + ',' + telefone + ',' + wrote + ';\n'
    with open('input_data_str.txt', 'a', encoding='utf-8') as f:
        f.write(res_data)
        print(f'добавлена запись - {res_data}')


def data():
    sec = ''
    nam = ''
    tel = ''
    wr = ''
    for count in range(4):
        if count == 0:
            sec = input('введите фамилию - ')
        elif count == 1:
            nam = input('введите имя - ')
        elif count == 2:
            tel = input('введите телефон - ')
        else:
            wr = input('введите описание - ')
    return sec, nam, tel, wr


if __name__ == "__main__":
    input_one_str()
    input_all_str()
