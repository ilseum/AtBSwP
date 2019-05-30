import random

print('I am thinking of a number between 1 and 20')
print('Take a guess')

randomNumber = random.randint(1, 20)
numberOfGuesses = 1
guess = int(input())

while guess != randomNumber:
    if guess < randomNumber:
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')

    numberOfGuesses += 1
    guess = int(input())

print('Good Job! You guessed my number in ' + str(numberOfGuesses) + ' guesses!')
