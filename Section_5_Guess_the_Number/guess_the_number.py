# In this example we will build a program which allows the user to guess number #

import random # to get a random number from the import module

print('Hello what is your name?')
print(r'Well {name} I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7): 
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

print(r'You took ' + str(guessesTaken) + ' guesses ' + 'the number was ' + str(secretNumber))