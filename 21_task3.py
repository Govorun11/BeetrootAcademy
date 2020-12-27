my_name = 'edik kudryavcev'
name = input('Введите ваше имя:\n')
if name.lower() in my_name:
    print(f'Добро пожаловать,{name}!')
else:
    print('Ты не мой хозяин')
