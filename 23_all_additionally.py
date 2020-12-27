'''
Asked a limit from a user, and print  all numbers excepts multiple of 18,
when the number will be 42, program prints "Because". Ignore the numbers between 50 to 80




limit = int(input('Insert int limit:'))
number = 0
while number != limit:
    number += 1
    if number % 18 != 0 and number != 42 and number < 50 or number > 80 :
        print(number)
        break cbvb  b gcv
    elif number == 42:
        print('Because')
'''
'''
Спросить у пользователя сколько попыток и до скольки максимум пробовать.
Сделать генерацию рендомного значения столько то раз.
Каждое значение вывести и потом вывести итоговое максимально ввыпавшее число.
Решение ЧЕРЕЗ СПИСОК.
'''
import random

limit = int(input('Insert limit number:\n'))
lenght_list = int(input('What lenght of list?\n '))
i = 0
l = []
while i != lenght_list:
    random_numbers = random.randint(0, limit)
    l.append(random_numbers)
    i += 1
print(l)
print('Max number from list: ', max(l))

