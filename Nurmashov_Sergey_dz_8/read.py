import json


def find_data(data, ls):
    user_enter = input('введите искомые данные - ')
    flag = 0
    for j in ls:
        if j[data] == user_enter:
            print('Совпадение найдено')
            for key, val in j.items():
                print(f'{key} - {val}')
                flag = 1
            break
    if not flag:
        print('Такого человека нет в базе')


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fr:
        json_str = fr.read()
        dataset = json.loads(json_str)

        print('Хотите просмотреть полностью базу данных '
              'или найти конкретного человека?'
              '\n1 - полностью базу\n2 - найти человека')
        user = int(input('Выберите вариант: '))
        if user == 1:  # полностью базу
            for i in dataset:
                for key, val in i.items():
                    print(f'{key} - {val}')
                print()
        else:  # поиск по конкретным данным
            print('По каким данным хотите найти?:'
                  '\n1 - id\n2 - Имя\n3 - Фамилия\n4 - Номер телефона')
            user_data = int(input('Выберите вариант: '))
            if user_data == 1:
                find_data('id', dataset)
            elif user_data == 2:
                find_data('name', dataset)
            elif user_data == 3:
                find_data('last_name', dataset)
            else:
                find_data('telefone', dataset)

        return dataset
