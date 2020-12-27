import random

my_word = list(input('Insert anything word: \n'))
random.shuffle(my_word)
mixed_word = ''.join(my_word)
print(f'Your mixed word look like this: {mixed_word}')
