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

