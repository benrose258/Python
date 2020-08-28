#Question 2
def checkletters(x,y):
    if x=="A" and y=="T":
        return True
    elif x=="T" and y=="A":
        return True
    elif x=="C" and y=="G":
        return True
    elif x=="G" and y=="C":
        return True
    else:
        return False

def mismatched_pairs(string1,string2):
    if len(string1)!=len(string2):
        return string1+" and "+string2+" DNA strings do not have the same length."
    else:
        counter=0
        for letter in range(len(string1)):
            if checkletters(string1[letter],string2[letter])==False:
                counter=counter+1
        return counter

#Question 3
def primes(x):
    for number in range(2,x):
        if x%number == 0:
            return False
        else:
            return True

def first_n_primes(n,mylist):
    if mylist == []:
        return "Error: There is no items in the list."
    else:
        for number in mylist:
            finallist=[]
            if primes(number)==True and len(finallist)<n:
                finallist.append(number)
                print number
        if n>len(finallist) and len(finallist)!=0:
            print "I only found "+str(len(finallist)+1)+" primes."
        if len(finallist)==0:
            print "I didn't find any primes."
            
