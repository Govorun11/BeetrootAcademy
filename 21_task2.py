number = input('Введите ваш номер телефона:\n'
               'Пример: +380ХХХХХХХХХ\n'
               '+38')

if number.isdigit() == True:
    if len(number) > 10:
        print('вы не правильно ввели номер')
    elif len(number) < 10:
        print('Вы не правильно ввели номер')
    else:
        print(f'Ваш номер +38{number}!')
else:
    print('Некоректный ввод!')
