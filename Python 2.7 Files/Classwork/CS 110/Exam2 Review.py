#2
def checkletters(a,b):
    if (a == "A") and (b == "T"):
        return True
    elif (a == "T") and (b == "A"):
        return True
    elif (a == "C") and (b == "G"):
        return True
    elif (a == "G") and (b == "C"):
        return True
    else:
        return False
    
def mismatched_pairs(string1,string2):
    if len(string1) != len(string2):
        print string1 + " and " + string2 + "DNA strings do not have the same length."
    else:
        counter = 0
        for index in range(len(string2)):
            if checkletters(string1[index],string2[index])==False:
                counter = counter + 1
        return counter

def printtheletters(mystring):
    for index in range(len(mystring)):
        print mystring[index]

def addtheletters(string1,string2):
    
    for index in range(len(string1)):
        print string1[index]
        print string2[index]

#3
def prime(x):
    for number in range(2,x):
        if x%number == 0:
            return False
    return True
def first_n_primes(n,mylist):
    finallist=[]
    for number in mylist:
        if prime(number) == True:
            finallist.append(number)
    if finallist==[]:
        print "I didn't find any primes."
    elif len(finallist)<n:
        for numbers in finallist:
            print numbers
        print "I only found "+str(len(finallist))+" primes."
    else:
        for index in range(n):
            print finallist[index]
