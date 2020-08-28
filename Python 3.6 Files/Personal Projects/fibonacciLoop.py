'''
Created on Mar 23, 2017

@author: Ben Rose
'''

def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)
    
def fib(number):
    if number == 0:
        return 'Error: no output'
    elif number == 1:
        return 0
    else:
        print(0)
        print(1)
        resultnumber = 1
        firstnumber = 0
        for number in range(0,number):
            print(resultnumber + firstnumber)
            firstnumber = resultnumber + firstnumber
            
print(fib(5))