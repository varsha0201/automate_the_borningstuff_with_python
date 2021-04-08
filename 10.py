# This is the guess the number program.

import random

print('Hello! What is your name?')
name = input()

print('Well' + str(name) + 'I am thinking number btween 1 - 20')
secreateNumber = random.randint(1, 20)

for guessesTaken in range(1,7):
    # logic
    print('Take a guess')
    guess = int(input())

    if guess < secreateNumber:
        print('Too low number')
    elif guess > secreateNumber:
        print(' Too high number')
    else:
        break

if guess == secreateNumber:
    print('Good job! ' + name+'you guess numeber in guess take is' + str(guessesTaken) +'.')
else:
    print('Number I was thinking of ' +str(secreateNumber)+'.')
print('You took ' + str(guessesTaken)+ ' gueeses.')