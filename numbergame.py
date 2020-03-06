# this is guess the number game

import random

print('Hello, What is your name?')
name = input()

print('Well, '+name+ ',I am thinking of a number between 1 to 20.')
secret_number = random.randint(1,20)

for guesstaken in range(1,7):
    print('guess no:')
    guess = int(input())
    if guess > secret_number:
        print('Your guess is too high.')
    elif guess < secret_number:
        print('Your guess is too low.')
    else:
        break # guess the accurate no

if guess == secret_number:
    print('Well done,'+name+',your have guessed correctnumber in '+ str(guesstaken)+' guess.')
else:
    print('Nope! The number I was thinking of was '+ str(secret_number)+'.')


