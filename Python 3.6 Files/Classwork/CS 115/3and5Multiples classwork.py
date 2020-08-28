'''
Created on May 2, 2017

@author: Ben Rose
'''
# Go to projecteuler.net for this problem (it is problem 1)
mysum = 0
for number in range(3,1000):
    if number % 3 == 0 or number % 5 == 0:
        mysum += number

print(mysum)
