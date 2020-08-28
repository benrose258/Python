'''
Created on Mar 23, 2017

@author: Ben Rose
'''
import sys

def divide(x,y):
    if not isinstance(x,int) and not isinstance(x,float):
        raise TypeError('x is not a number.')
    elif y == 0:
        raise ZeroDivisionError('Cannot divide ' + str(x) + ' by 0.')
    else:
        return x/y

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print('You did not enter a valid integer.')

def getString(prompt):
    mystring = input(prompt)
    if len(mystring) > 10:
        raise ValueError('String exceeds max length 10 characters.')
    else:
        return mystring

try:
    name = getString('Enter your name: ')
except ValueError as error:
    print('Error:', error)
    sys.exit(1)

try:
    print(divide(len(name),2))
except (ZeroDivisionError, TypeError) as error:
    print('Error:',error)

sys.exit(0)
