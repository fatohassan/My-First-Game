# This is the guess number game

import random
print('Hello, What is your name? ')
name = input()

print('Well ' + name + '! I was thinking of a number between 1 and 20')
secretNum = random.randint(1,20)

for guessTaken in range(1,7):
    print('Take a guess! ')
    guess = int(input())
    if guess < secretNum:
        print('Your guess is too low')
    elif guess > secretNum:
        print('Your guess is too high')
    else:
        break
if guess == secretNum:
    print('Great! your guess is correct')
else:
    print('Nope. The number I was thinking of is ' + str(secretNum)) 
    
