def input_from_file():
    """ импорт осуществляется с файла """

    with open('data.txt', 'r', encoding='utf-8') as file:
        for i in file:
            if i.find(',') == -1:
                print(i.replace('\n', ''))
                with open('input_data.txt', 'a', encoding='utf-8') as f:
                    f.write(i)
            else:
                print(i.replace('\n', ';'))
                res_data = i.replace('\n', ';\n')
                with open('input_data_str.txt', 'a', encoding='utf-8') as f:
                    f.write(res_data)


if __name__ == "__main__":
    input_from_file()
