'''
Created on Jan 31, 2017

@author: Ben Rose
'''

from cs115 import reduce
from clear import clear
from lab2 import even,odd

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def tower(n):
    if n == 0:
        return 1
    else:
        return 2**tower(n-1)

def power(x,y):
    return y**x

def tower_reduce(n):
    return reduce(power,[2]*n)

def length(mylist):
    if mylist == []:
        return 0
    else:
        return 1 + length(mylist[1:])

def reverse(mylist):
    if mylist == []:
        return []
    else:
        return [mylist[-1]] + reverse(mylist[0:-1])

def mystery(n):
    return m_help(n,0)

def m_help(n,r):
    if n == 0:
        return r
    return m_help(n//10, r*10 + n % 10)

'''"Mystery" function is tail recursion. Tail recursion occurs when there are no pending operations.
The result of the function call at the base case is the final answer. There is no need to trace
back up and apply the result.'''

def member(x, mylist):
    if mylist == []:
        return False
    elif mylist[0] == x:
        return True
    else:
        return member(x,mylist[1:])

def mymap(myfunc,mylist):
    if mylist == []:
        return []
    else:
        return [myfunc(mylist[0])] + mymap(myfunc,mylist[1:])

def add(x,y):
    return x + y

def myreduce(myfunc,mylist):
    if mylist == []:
        return "Error"
        raise TypeError("Error: Empty list.")
    if mylist[:-1] == []:
        return mylist[-1]
    return myfunc(myreduce(myfunc,mylist[:-1], mylist[-1]))

def double(mynumber):
    return 2 * mynumber

def sieve(mylist):
    if mylist == []:
        return []
    else:
        return [mylist[0]] + sieve(filter(lambda x: x % mylist[0] != 0, mylist[1:]))

def primes(mynumber):
    return sieve(range(2,n+1))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def powerset(mylist):
    if mylist == []:
        return [[]]
    else:
        use_it = map(lambda subset: [mylist[0]] + subset, lose_it)
        lose_it = powerset(mylist[1:])
        return use_it+lose_it

def subset(target, lst):
    if target == 0:
        return True
    elif lst == []:
        return False
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

def subset2(target, lst):
    if target == 0:
        return True
    elif lst == []:
        return False
    use_it = subset(target - lst[0], lst[1:])
    lose_it = subset(target, lst[1:])
    return use_it or lose_it

def SwithV(target, lst):
    if target == 0:
        return (True, [])
    elif lst == []:
        return (False, [])
    use_it = SwithV(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return SwithV(target, lst[1:])

def cointest(mylist):
    if mylist == []:
        return 0
    else:
        useIt = mylist[0] + cointest(mylist[2:])
        loseIt = cointest(mylist[1:])
        return max(useIt, loseIt)

def cointest2(mylist):
    if mylist == []:
        return 0
    return max(mylist[0] + cointest2(mylist[2:]), cointest(mylist[1:]))

def cointestlist(mylist):
    if mylist == []:
        return (0,[])
    else:
        useIt = cointestlist(mylist[2:])
        newsum = mylist[0] + useIt[0]
        loseIt = cointestlist(mylist[1:])
        if newsum > loseIt[0]:
            return (newsum, [mylist[0]] + useIt[1])
        else:
            return loseIt

'''LCS: Longest Common Subsequence. Data for this function is in Powerpoint 9 near the end from CS 110.
   This will return the length of longest common sequence from left to the right of the two strings.'''

def LCS(string1,string2):
    if string1 == '' or string2 == '':
        return 0
    elif string1[0] == string2[0]:
        return 1 + LCS(string1[1:],string2[1:])
    else:
        return max(LCS(string1,string2[1:]),LCS(string1[1:],string2[1:]))

def subset(target,mylist):
    '''Checks if we can get target down to zero by subtracting the numbers available
       in mylist. If it can't, using every combination, then it returns False. If there is
       at least one combination that works, then return True.'''
    if target == 0:
        return True
    elif mylist == []:
        return False
    elif mylist[0] > target:
        return subset(target,mylist[1:])
    else:
        useIt = subset(target-mylist[0],mylist[1:])
        loseIt = subset(target,mylist[1:])
        return useIt or loseIt

def LCS(string1,string2):
    '''This is the same as the other LCS, except more written out. Because we are only referencing useS1 and useS2 once, we don't need to make them variables.'''
    if string1 == '' or string2 == '':
        return 0
    elif string1[0] == string2[0]:
        return 1 + LCS(string1[1:],string2[1:])
    else:
        useS1 = LCS(string1,string2[1:])
        useS2 = LCS(string1[1:],string2)
        return max(useS1,useS2)

def LCSWithValues(string1,string2):
    '''Returns the length of the longest common subsequence in strings string1 and string2, as well as the string of common characters.
       The result will be a tuple.'''
    if string1 == '' or string2 == '':
        return (0,'')
    elif string1[0] == string2[0]:
        result = LCSWithValues(string1[1:],string2[1:])
        return (1 + result[0], string1[0] + result[1])
    else:
        useS1 = LCSWithValues(string1,string2[1:])
        useS2 = LCSWithValues(string1[1:],string2)
        if useS1[0] > useS2[0]:
            return useS1
        else:
            return useS2

def distance(string1,string2):
    if string1 == '':
        return len(string2)
    elif string2 == '':
        return len(string1)
    elif string1[0] == string2[0]:
        return distance(string1[1:],string2[1:])
    else:
        #Sub: you made one change, removing the first letter of them. So that is one change 'turn'.
        #Del: you made one change, removing the first letter of string1. So that is another change 'turn'.
        #Ins: you made one change, removing the first letter of string2. So that is yet another change 'turn'.
        #The return 1 + ... at the end is an optimization: it can also be 1+sub,1+del, and 1+ins.
        substitution = distance(string1[1:],string2[1:])
        deletion = distance(string1[1:],string2)
        insertion = distance(string1,string2[1:])
        return 1 + min(substitution,deletion,insertion)

def distanceWithValues(string1,string2):
    if string1 == '':
        return (len(string2),string2)
    elif string2 == '':
        return (len(string1),string1)
    elif string1[0] == string2[0]:
        return distanceWithValues(string1[1:],string2[1:])
    else:
        subResult = distanceWithValues(string1[1:],string2[1:])
        substitution = (1 + subResult[0],'')

        delResult = distanceWithValues(string1[1:],string2)
        deletion = (1 + delResult[0],string2[0])

        insResult = distanceWithValues(string1,string2[1:])
        insertion = (1 + insResult[0],string1[0])
        if substitution[0] < deletion[0] and substitution[0] < insertion[0]:
            return substitution
        elif deletion[0] < substitution[0] and deletion[0] < insertion[0]:
            return deletion
        else:
            return insertion

def ED(string1,string2):
    '''Detects if string1 and string2 are different at indices in
       the strings. If they are, then we leave it be. If they are not, then we add 1 and
       continue on. This will return the number of differences at other points.'''
    if string1 == '':
        return len(string2)
    elif string2 == '':
        return len(string1)
    elif string1[0] == string2[0]:
        return ED(string1[1:],string2[1:])
    else:
        useS1 = 1 + ED(string1,string2[1:])
        useS2 = 1 + ED(string1[1:],string2)
        loseBoth = 1 + ED(string1[1:],string2[1:])
        return min(useS1,useS2,loseBoth)
