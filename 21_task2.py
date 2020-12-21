number = input('Введите ваш номер телефона:\n'
               'Пример: +380-ХХ-ХХ-ХХХ-ХХ\n'
               '+38')
while number !=10:
    if number.isdigit() == True:
        if len(number) > 10:
            print('вы не правильно ввели номер')
            break
        elif len(number) < 10:
            print('Вы не правильно ввели номер')
            break
        else:
            print('Ваш номер +38'+number)
            break
    else:
        print('Некоректный ввод')
        break