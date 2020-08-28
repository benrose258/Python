#I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''
Created on Jan 27, 2017

@author: Ben Rose
'''

import math

from cs115 import map, reduce, range

def add(x,y):
    '''Adds 2 numbers and returns the result.'''
    return x + y

def inverse(n):
    """Given an input n, returns the reciprocal of the number in decimal form."""
    return 1/n

def reciprocal(mylist):
    return map(inverse,map(math.factorial,mylist))

def e(n):
    '''Given an input n, it returns n! of the number.'''
    mylist = map(inverse,map(math.factorial,range(1,n+1)))
    return 1+reduce(add,mylist)

def error(n):
    return abs(math.e-e(n))