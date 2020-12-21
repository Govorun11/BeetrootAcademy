n_str = input('Придумайте любое слово:\n')
while len(n_str) >= 2:
    print(n_str[:2] + n_str[-2:])
    break
else:
    print('Введите слово длиннее!')

