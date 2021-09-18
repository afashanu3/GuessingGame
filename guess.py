import random

def guess(x):

    random_number = random.randint(1,x9)
    guess = 0

    while guess != random_number:
        guess =int(input(f'Guess a number between 1 and 19'))
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')
        else:
            print("You guessed it buddy")

guess(10)
