import json


def find_data(data, ls):
    user_enter = input('введите искомые данные - ')
    flag = 0
    for j in ls:
        if j[data] == user_enter:
            print('Совпадение найдено')
            ls.remove(j)
            flag = 1
            break
    if not flag:
        print('Такого человека нет в базе')
    return ls


def delete_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fr:
        json_str = fr.read()
        dataset = json.loads(json_str)

        print('Хотите удалить полностью базу данных '
              'или удалить данные конкретного человека?'
              '\n1 - удалить полностью базу\n2 - удалить данные конкретного человека')
        user = int(input('Выберите вариант: '))
        if user == 1:  # полностью базу
            with open(file_name, 'w', encoding='utf-8') as fw:
                dataset.clear()
                json_str = json.dumps(dataset, ensure_ascii=False, indent=2)
                fw.write(json_str)
                print('Удаление завершено')
        else:  # удалить по конкретным данным
            print('По каким данным хотите найти и удалить?:'
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
                print('Удаление завершено')
