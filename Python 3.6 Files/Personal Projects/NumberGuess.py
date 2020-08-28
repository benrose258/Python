'''
Created on Mar 28, 2017

@author: Ben Rose
'''
import random

MAX_TRIES = 7

print('''---Welcome to Guess My Number ---

I'm thinking of a number between 1 and 100.
Try to guess the number in %d''' % MAX_TRIES, end='')
# %d is placeholder for an integer
# %f is placeholder for a float
# %s is placeholder for a string
# end='' means to not bring the cursor down to the next line, so it would keep in this case the word next to it instead of on the next line

if MAX_TRIES == 1:
    print(' attempt...')
else:
    print(' attempts...')

# Set the initial values
number = random.randint(1,100) # generates a random number in [1,100] (using this it includes 100)
tries = 1
guess = int(input('Enter guess %d: ' % tries))

# Guessing loop
while guess != number:
    if guess > number:
        print('Lower...')
    else:
        print('Higher...')

    tries += 1
    if tries > MAX_TRIES:
        break
    guess = int(input('Enter guess %d: ' % tries))

if tries <= MAX_TRIES:
    print('\nCongratulations! You correctly guessed the number %d and it took you only %d' % (number, tries), end = '')
else:
    print('\nSorry, you did not guess the number %d in %d' % (number, MAX_TRIES), end = '')

if MAX_TRIES == 1:
    print(' try.')
else:
    print(' tries.')
