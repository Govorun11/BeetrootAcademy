"""когда my_name == name, не работает принтует почему то,
но когда my_name != name, принт работает(((( """


my_name = 'Edik'
name = input('Введите ваше имя:\n')
if name.lower().find('edik'):
    if my_name == name:
        print('Добро пожаловать, !'+my_name)
    else:
        print('Ты не мой хозяин')



