'''
Created on Sep 11, 2017

@author: Ben Rose
'''
import math

def onesum(n):
    total = 0
    for k in range(1,n):
        total += ((3**k * 10**-k*(-1)**k+1)/math.factorial(k))
    return total

print(onesum(5))