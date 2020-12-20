# комп угадывает число от 1 до 100!

import random

print('Давай сыграем в игру=)'
      'Загадайте число от 1 до 100, а я попробую угадать=)')

min, max = 1, 100
while min != max:
    midle = (min + max) // 2
    yes_no = input(f'Ты загадал число{midle} ?')
    if yes_no.lower().find('yes') >= 0:
        print('Я угадал!')
        break
    else:
        more_less = input('Твое число меньше?')
    if more_less.lower().find('no'):
        max = midle - 1
        print(random.randint(min, max))
    else:
        min = midle + 1
else:
    print('Врунишка!=Р')

# elif:
# print(input('Твое число больше?', y)
# else:
# print (input('Твое число больше?'), n)
