name = input('Insert your name:\n')
age = input('Insert your age: \n')
if age.isdigit() and name.isalpha():
    print(f"Hello, {name.title()}, on your next birthday you'll be {int(age) + 1}")
else:
    print('Insert your date like in example:\n'
          'Insert Your name: Edik\n'
          'Insert Your age: 21')
