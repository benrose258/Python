#I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
#Question 2

def replace(x,y,mylist):
    if mylist==[]:
        return []
    else:
        if mylist[0]==x:
            return [y]+replace(x,y,mylist[1:])
        else:
            return [mylist[0]]+replace(x,y,mylist[1:])

#Question 3

def prime(x):
    for denominator in range(2,x):
        if x%denominator == 0:
            return False
    return True

def primes(mylist):
    if mylist==[]:
        return []
    elif prime(mylist[0])==True:
        return [mylist[0]]+primes(mylist[1:])
    else:
        return primes(mylist[1:])

def first_n_primes(primelimit,mylist):
    primeList=primes(mylist)
    if primeList == []:
        print "I didn't find any primes."
    elif len(primeList)<primelimit:
        for index in primeList:
            print index
        print "I only found "+str(len(primeList))+" primes."
    else:
        for index in range(primelimit):
            print primeList[index]

#Question 4

def findBlack(code,guess,colors):
    return helperfunc(code,guess,colors*[0],[])

def helperfunc(code,guess,colors,matches):
    if code == []:
        return [matches,colors]
    else:
        if code[0]==guess[0]:
            colors[code[0]] = colors[guess[0]] + 1
            return helperfunc(code[1:],guess[1:],colors,matches+["black"])
        else:
            return helperfunc(code[1:],guess[1:],colors,matches+["dummy"])
