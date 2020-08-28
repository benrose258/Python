'''
Created on Aug 30, 2017

@author: Ben Rose
'''
def dot(setA,setB):
    if setA == [] or setB == []:
        return 0
    else:
        return setA[0]*setB[0] + dot(setA[1:],setB[1:])

def explode(mystring):
    if mystring == '':
        return []
    else:
        return [mystring[0]] + explode(mystring[1:])

def ind(e,mylist):
    if len(mylist) == 0:
        return 0
    elif mylist[0] == e:
        return 0
    else:
        return 1 + ind(e,mylist[1:])

def removeAll(e,mylist):
    if mylist == []:
        return []
    elif mylist[0] == e:
        return removeAll(e,mylist[1:])
    else:
        return [mylist[0]] + removeAll(e,mylist[1:])

def myFilter(func,mylist):
    if mylist == []:
        return []
    elif func(mylist[0]) == True:
        return [mylist[0]] + myFilter(func,mylist[1:])
    else:
        return myFilter(func,mylist[1:])
    
def deepReverse(mylist):
    if mylist == []:
        return []
    elif type(mylist[-1]) == list:
        return [deepReverse(mylist[-1])] + deepReverse(mylist[:-1])
    else:
        return [mylist[-1]] + deepReverse(mylist[:-1])
    