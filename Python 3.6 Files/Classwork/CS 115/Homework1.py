#I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose

'''
Created on Jan 27, 2017

@author: Ben Rose
'''

from cs115 import map, reduce

def add(x,y):
    '''Returns the sum of two numbers.'''
    return x+y

def multiply(x,y):
    '''Returns the product of two numbers.'''
    return x*y

def factorial(n):
    '''Returns the n! of a number n.'''
    if n <= 0:
        return "Error: Non-positive input"
    else:
        return reduce(multiply,range(1,n+1))

def mean(mylist):
    '''Returns the mean value of all the numbers in a provided list.'''
    length = len(mylist)
    reduction = reduce(add,mylist)
    return reduction/length

def prime(n):
    for number in range(2,n):
        if n % number == 0:
            return False
    return True
