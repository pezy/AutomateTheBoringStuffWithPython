#!python3
# coin_toss.py - a simple coin toss guessing game. The player gets two guesses.

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = ('heads', 'tails')[random.randint(0, 1)]  # 0 is tails, 1 is heads

assert toss in ('heads', 'tails'), 'toss should be heads or tails.'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
