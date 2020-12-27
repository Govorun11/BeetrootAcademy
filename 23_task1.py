import random

print('Hello! lets play in game!'
      'Try to guess int number between 0 and 10!')
user_number = int(input('Insert your number: '))
computer_number = random.randint(1, 10)
if user_number <= 10 and user_number >= 0:
    if user_number == computer_number:
        print('You WIN!')
    else:
        print(f"Does not guess. Computer's number is {str(computer_number)}!")
        print('Try again!')
else:
    print('Invalid number. Please, choose a number between 0 and 10!')
