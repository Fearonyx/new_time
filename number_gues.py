# Угадай число
import random

answer = random.randint(1,101)
guess = 0
while guess != answer:
    guess = int(input('Input your number: '))
    if guess < answer:
        print('Greater')
    elif guess > answer:
        print('Lower')
    else:
        print('You are win!!!')

