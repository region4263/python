import inputdata
import inputdatafile
import out

print('введите вариант работы:\n'
      '1. импорт в телефонный справочник\n'
      '2. экспорт из телефонного справочника')
enter = int(input())

if enter == 1:  # импорт в телефонный справочник
    print('импорт будет осуществляться:\n1. вручную\n2. с файла')
    inp = int(input())
    if inp == 1:  # вручную
        print('1. на одной строке хранится одна часть записи\n'
              '2. на одной строке хранятся все записи')
        data = int(input(''))
        if data == 1:
            inputdata.input_one_str()
        else:
            inputdata.input_all_str()
    else:  # с файла
        inputdatafile.input_from_file()
else:  # экспорт из телефонного справочника
    print('экспорт будет осуществляться:\n'
          '1. на одной строке хранится одна часть записи\n'
          '2. на одной строке хранятся все записи')
    exp = int(input(''))
    if exp == 1:
        out.out_one_str()
    else:
        out.out_all_str()
