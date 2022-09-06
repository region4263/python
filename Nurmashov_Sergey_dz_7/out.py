def out_one_str():
    """  вывод данных справочника: на одной строке одна часть записи """
    with open('data.txt', 'r', encoding='utf-8') as f:
        for data in f:
            if data.find(',') == -1:
                print(data.replace('\n', ''))
            else:
                print(data.replace(',', '\n')[:-1] + '\n')


def out_all_str():
    """  вывод данных справочника в одну строку """
    with open('data.txt', 'r', encoding='utf-8') as f:
        data_1 = ''
        count = 0
        for data in f:
            if data == '\n':
                pass
            elif data.find(',') == -1 and count < 3:
                data_1 += data.replace('\n', '') + ','
                count += 1
            elif data.find(',') == -1 and count == 3:
                data_1 += data.replace('\n', ';')
                print(data_1)
                data_1 = ''
                count = 0
            else:
                print(data.replace('\n', ';'))


if __name__ == "__main__":
    out_one_str()
    out_all_str()
