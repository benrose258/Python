#Question 4

def member(x,mylist):
    if mylist == []:
        return False
    elif mylist[0] == x:
        return True
    else:
        return member(x,mylist[1:])

#Question 11

D = {}

def memosubset(target,mylist):
    if target == 0:
        return True
    elif mylist == []:
        return False
    elif target < mylist[0]:
        return memosubset(target,mylist[1:])
    elif (target,tuple(mylist)) in D:
        return D[(target,tuple(mylist))]
    else:
        useIt = memosubset(target-mylist[0],mylist[1:])
        loseIt = memosubset(target,mylist[1:])
        optimal = useIt or loseIt
        D[(target,tuple(mylist))] = optimal
        return optimal

#Question 8

def evens(mylist):
    if mylist == []:
        return []
    elif mylist[0] % 2 == 0:
        return [mylist[0]] + evens(mylist[1:])
    else:
        return evens(mylist[1:])

#Question 7

def palindrome(mystring):
    if mystring == "":
        return True
    elif mystring[0] == mystring[-1]:
        return palindrome(mystring[1:-1])
    else:
        return False

#Question 6

def uniquify(mylist):
    if mylist == []:
        return []
    elif member(mylist[0],mylist[1:]):
        return uniquify(mylist[1:])
    else:
        return [mylist[0]]+uniquify(mylist[1:])

#Question 3

def bump(mylist):
    if mylist == []:
        return []
    else:
        return [mylist[0]+1] + bump(mylist[1:])

def succ(mynumber):
    return mynumber+1
