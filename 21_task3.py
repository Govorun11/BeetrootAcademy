"""когда my_name == name, не работает принтует почему то,
но когда my_name != name, принт работает(((( """

name = 'edik'
my_name = input('Введите ваше имя:\n')
if my_name.lower()in name:
    print('Добро пожаловать, '+my_name)
else:
        print('Ты не мой хозяин')



