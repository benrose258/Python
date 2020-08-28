'''
Created on Mar 28, 2017

@author: Ben Rose
'''
import random

def leppard(input_string):
    output_string = ''
    for symbol in input_string:
        if symbol == 'o':
            output_string = output_string + 'ooo'
        else:
            output_string = output_string + symbol
    return output_string

vowels = ['a', 'e', 'i', 'o', 'u']

def spamify(word):
    for i in range(len(word)):
        if word[i] not in vowels:
            return word[0:i] + 'spam' + word[i+1:]
    return word

def mapSqr(mylist):
    finallist = []
    for number in mylist:
        finallist.append(number * number)
    return finallist

def mapSqr2(mylist):
    return [number * number for number in mylist]

def average(mylist):
    mysum = 0
    for number in mylist:
        mysum = mysum + number
    return mysum/len(mylist)

def find_max(mylist):
    '''Returns the maximum value in mylist. If the list is empy, returns None.'''
    if mylist == []:
        return None
    else:
        mymax = mylist[0]
        for number in mylist:
            if number > mymax:
                mymax = number
        return mymax

def find_min(mylist):
    '''Returns the minimum value in mylist. If the list is empty, returns None.'''
    if mylist == []:
        return None
    else:
        mymin = mylist[0]
        for number in mylist:
            if number < mymin:
                mymin = number
        return mymin

def findMinMax(mylist):
    if mylist == []:
        return None
    else:
        mymin = mymax = mylist[0]
        for number in mylist:
            if number > mymax:
                mymax = number
            elif number < mymin:
                mymin = number
        return (mymin,mymax)

def shallowCopy(mylist):
    return [number for number in mylist]

def deepCopy(mylist):
    finallist = []
    for index in mylist:
        if type(index) is list:
            finallist.append(deepCopy(index))
        else:
            finallist.append(index)
    return finallist

def sumMatrix(matrix):
    mysum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            mysum += matrix[row][col]
    return mysum

def sumMatrix2(matrix):
    mysum = 0
    for row in matrix:
        for index in row:
            mysum += index
    return mysum

def printMatrix(matrix):
    for row in range(len(matrix)):
        print(' ', end='')
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=' ')
            if col < 2:
                print('| ',end = '')
        print()
        if row < 2:
            print('-'*11)
