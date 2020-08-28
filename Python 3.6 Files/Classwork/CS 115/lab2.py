#I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''
Created on Feb 2, 2017

@author: Ben Rose
'''

def dot(mylist1, mylist2):
    '''First, the function checks if either of the two lists are empty. If it is empty, the function returns 0.0. If not, the function
    returns the product of first item in mylist1 and mylist2, then restarts the function excluding the items in the list that were
    just tested. The output of the function will be a number, either 0.0 if either of the lists were empty to begin with, or the sum of the
    products of the items in the list if not.'''
    if mylist1 == [] or mylist2 == []:
        return 0.0
    else:
        return mylist1[0]*mylist2[0] + dot(mylist1[1:], mylist2[1:])

def explode(mystring):
    '''This function takes the string provided and returns a list of every letter in the string put one after the other. It will
    keep going recursively until there are no more items left in the string, in which case it will add an empty list to the current
    list of characters. If the string is empty, then the function will return an empty list.'''
    if mystring == '':
        return []
    else:
        return [mystring[0]]+explode(mystring[1:])

def ind(item,mysequence):
    '''This function will search the provided list or string for the element provided by the user. If the sequence does not contain the
    item, the function will return the length of the original sequence. If the sequence does contain the element, however, the function
    will return the index of the first time the element appeared in the sequence. If the sequence is empty, it will return 0, as that is
    the length of the sequence.'''
    if mysequence == [] or mysequence == '':
        return 0
    elif item == mysequence[0]:
        return 0
    else:
        return 1 + ind(item,mysequence[1:])

def removeAll(item,mylist):
    '''This function searches the provided list for the item specified. If the item is found in the list, the item is removed from the
    resulting list. The function will then return the list without any instances of the provided item.'''
    if mylist == []:
        return []
    elif mylist[0] == item:
        return removeAll(item,mylist[1:])
    else:
        return [mylist[0]] + removeAll(item,mylist[1:])

def even(mynumber):
    '''This function checks of a provided number is even by checking if the number is evenly divisible by 2. If the quotient is not an
    integer (the remainder is not 0), then it is odd. If not it is even. If the number is even, the function returns True, if not,
    the function returns False.'''
    if mynumber % 2 == 0:
        return True
    else:
        return False

def odd(mynumber):
    '''This function checks of a provided number is odd by checking if the number is evenly divisible by 2. If the quotient is not an
    integer (the remainder is not 0), then it is odd. If not it is even. If the number is odd, the function returns True, if not,
    the function returns False.'''
    if mynumber % 2 == 0:
        return False
    else:
        return True

def myFilter(condition,mylist):
    '''This function uses the conditional statement provided and checks it against the provided list. If an item in the list does
    not meet the conditional statement, then the function removes that number from the returned list. If not, the item is included
    in the returned list. If the list is empty, the function will return an empty list.'''
    if mylist == []:
        return []
    elif condition(mylist[0]) == False:
        return myFilter(condition,mylist[1:])
    else:
        return [mylist[0]] + myFilter(condition,mylist[1:])

def deepReverse(mylist):
    '''This function takes in a list and, if the items in the list are not lists, returns the items in reverse order. If the function
    does come across a list within the lists, however, the list is reversed and added to the final list.'''
    if mylist == []:
        return []
    elif isinstance(mylist[-1],list) == True:
        return [deepReverse(mylist[-1])] + deepReverse(mylist[0:-1])
    else:
        return [mylist[-1]] + deepReverse(mylist[0:-1])
