# Угадай число
import random


# Компьютер загадывает число в пределах от 1 до 100 включительно
def what_number():
    return random.randrange(1, 101)


def user_inp():
    user_input = int(input('Input your number: '))
    return user_input


def game():
    comp_number = what_number()
    user_number = user_inp()
    while user_number != comp_number:
        if user_number > comp_number:
            print('Nope. Lower.')
        elif user_number < comp_number:
            print('Greater')
        user_number = user_inp()
    print('You are win!!!')
    print("Let's play again")
    game()


game()
