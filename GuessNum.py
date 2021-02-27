import random

def guess(x):
    guess = 0
    random_num = random.randint(1,x)
    while(guess != random_num):
        guess = int(input(f'Guess a number between 1 and {x}: '))
    print(f'Correct the num was {random_num}')
    
guess(10)