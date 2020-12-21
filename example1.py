# комп угадывает число от 1 до 100!
# при запуске кода

import random

print('Давай сыграем в игру=)\n'
      'Загадайте число от 1 до 100, а я попробую угадать=)')

min, max = 0, 100
while min != max:
    midle = (min + max) // 2
    yes_no = input(f'Ты загадал число{midle} ?')
    if yes_no.lower().find('yes') >= 0:
        print('Я угадал!')
        break
    else:
        yes_no = input('Твое число больше?');
    if yes_no.lower().find('yes'):
        max = midle - 1
        print(random.randint(min, max))
    elif yes_no.lower().find('no'):
        min = midle + 1
    else:
        pass
else:
    print('Врунишка=Р')
