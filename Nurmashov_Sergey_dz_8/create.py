import json


def write_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fr:
        json_str = fr.read()
        dataset = json.loads(json_str)

    with open(file_name, 'w', encoding='utf-8') as fw:
        key_max = 0
        for i in dataset:
            for _ in i:
                if key_max < int(i["id"]):
                    key_max = int(i["id"])

        data = dict()
        data['id'] = str(key_max + 1)
        data['name'] = input('введите имя - ')
        data['last_name'] = input('введите фамилию - ')
        data['telefone'] = input('введите телефон - ')

        dataset += [data]

        json_str = json.dumps(dataset, ensure_ascii=False, indent=2)
        fw.write(json_str)
        print('запись завершена')
