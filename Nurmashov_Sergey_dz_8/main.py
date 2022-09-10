import create
import read
import update
import delete


print('Возможные функции: \n1. запись\n2. чтение\n3. удаление\n4. обновление')
user = int(input('выберите действие: '))
if user == 1:  # запись
    create.write_file('poi.json')
elif user == 2:  # чтение
    read.read_file('poi.json')
elif user == 3:  # удаление
    delete.delete_file('poi.json')
else:  # обновление
    update.update_file('poi.json')
