from telegram import Update
from telegram.ext import ContextTypes


def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return update.message.reply_text(f'введите вариант работы:\n'
                                     '1. импорт в телефонный справочник вручную '
                                     '(на одной строке хранится одна часть записи) /input_one_str\n'
                                     '2. импорт в телефонный справочник вручную '
                                     '(на одной строке хранятся все записи) /input_all_str\n'
                                     '3. импорт в телефонный справочник c файла /input_from_file\n'
                                     '4. экспорт из телефонного справочника'
                                     '(на одной строке хранится одна часть записи) /out_one_str\n'
                                     '5. экспорт из телефонного справочника '
                                     '(на одной строке хранятся все записи) /out_all_str')


def input_one_str_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """импорт в телефонный справочник вручную
        (на одной строке хранится одна часть записи)"""

    # вводить данные через пробел --> /input_one_str Сергей Морозов +79885554433 повар
    msg = update.message.text

    item = msg.split()
    sec_name = item[1]
    name = item[2]
    telefone = item[3]
    wrote = item[4]

    res_data = sec_name + '\n' + name + '\n' + telefone + '\n' + wrote + '\n' + '\n'
    with open('input_data.txt', 'a', encoding='utf-8') as f:
        f.write(res_data)
        print(f'добавлена запись:\n{res_data}')

    return update.message.reply_text(f'фамилия - {sec_name}\nимя - {name}\n'
                                     f'телефон - {telefone}\nописание - {wrote}\n'
                                     f'введены в телефонный справочник')


def input_all_str_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """импорт в телефонный справочник вручную
        (на одной строке хранятся все записи)"""

    # вводить данные через пробел --> /input_all_str Сергей Морозов +79885554433 повар
    msg = update.message.text

    item = msg.split()
    sec_name = item[1]
    name = item[2]
    telefone = item[3]
    wrote = item[4]

    res_data = sec_name + ',' + name + ',' + telefone + ',' + wrote + ';\n'
    with open('input_data_str.txt', 'a', encoding='utf-8') as f:
        f.write(res_data)
        print(f'добавлена запись - {res_data}')

    return update.message.reply_text(f'фамилия - {sec_name}\nимя - {name}\n'
                                     f'телефон - {telefone}\nописание - {wrote}\n'
                                     f'введены в телефонный справочник')


def input_from_file_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """импорт в телефонный справочник c файла"""

    with open('data.txt', 'r', encoding='utf-8') as file:
        for i in file:
            if i.find(',') == -1:
                with open('input_data.txt', 'a', encoding='utf-8') as f:
                    f.write(i)
                return update.message.reply_text('данные введены в телефонный справочник')
            else:
                res_data = i.replace('\n', ';\n')
                with open('input_data_str.txt', 'a', encoding='utf-8') as f:
                    f.write(res_data)
                return update.message.reply_text('данные введены в телефонный справочник')


def out_one_str_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """экспорт будет осуществляться:
        на одной строке хранится одна часть записи"""

    with open('data.txt', 'r', encoding='utf-8') as f:
        item = ''
        for data in f:
            if data.find(',') == -1:
                data.replace('\n', '')
                item += data
            else:
                data.replace(',', '\n')
                item += data

        return update.message.reply_text(item)


def out_all_str_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """экспорт будет осуществляться:
        на одной строке хранятся все записи"""

    with open('data.txt', 'r', encoding='utf-8') as f:
        data_1 = ''
        data_2 = ''
        count = 0
        for data in f:
            if data == '\n':
                pass
            elif data.find(',') == -1 and count < 3:
                data_1 += data.replace('\n', '') + ','
                count += 1
            elif data.find(',') == -1 and count == 3:
                data_1 += data.replace('\n', ';\n')
                data_2 += data_1
                data_1 = ''
                count = 0
            else:
                data_2 += data.replace('\n', ';\n')

    return update.message.reply_text(data_2)
