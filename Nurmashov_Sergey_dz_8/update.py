import json


def find_data(data, ls):
    user_enter = input('введите искомые данные - ')
    for j in ls:
        if j[data] == user_enter:
            print('Совпадение найдено')
            for key, val in j.items():
                print(f'{key} - {val}')
            print('Какие данные подлежат обновлению?'
                  '\n1 - Имя\n2 - Фамилия\n3 - Телефон')
            user = int(input('Выберите вариант: '))
            if user == 1:
                j['name'] = input('Введите новые данные: ')
            elif user == 2:
                j['last_name'] = input('Введите новые данные: ')
            else:
                j['telefone'] = input('Введите новые данные: ')
            break
    return ls


def update_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fr:
        json_str = fr.read()
        dataset = json.loads(json_str)

        print('По каким данным найти человека?:'
              '\n1 - id\n2 - Имя\n3 - Фамилия\n4 - Номер телефона')
        user_data = int(input('Выберите вариант: '))
        if user_data == 1:
            dataset = find_data('id', dataset)
        elif user_data == 2:
            dataset = find_data('name', dataset)
        elif user_data == 3:
            dataset = find_data('last_name', dataset)
        else:
            dataset = find_data('telefone', dataset)

        with open(file_name, 'w', encoding='utf-8') as fw:
            json_str = json.dumps(dataset, ensure_ascii=False, indent=2)
            fw.write(json_str)
            print('запись завершена')
