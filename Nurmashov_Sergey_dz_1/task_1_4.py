number = int(input('введите номер четверти - '))

if number == 1:
    print('координата Х:  от 0 до +бесконечность', 'координата Y:  от 0 до +бесконечность', sep='\n')
elif number == 2:
    print('координата Х:  от -бесконечность до 0', 'координата Y:  от 0 до +бесконечность', sep='\n')
elif number == 3:
    print('координата Х:  от -бесконечность до 0', 'координата Y:  от -бесконечность до 0', sep='\n')
else:
    print('координата Х:  от 0 до +бесконечность', 'координата Y:  от -бесконечность до 0', sep='\n')
