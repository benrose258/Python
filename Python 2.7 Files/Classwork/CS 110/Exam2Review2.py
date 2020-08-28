#Exam 2 Review, redone for extra practice

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
        for index in range(len(string1)):
            if checkletters(string1[index],string2[index])==False:
                counter=counter+1
        return counter

#Question 3

def prime(x):
    for d in range(2,x):
        if x%d == 0:
            return False
    return True

def first_n_primes(n,mylist):
    finallist = []
    for number in mylist:
        if prime(number)==True:
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

#Question 2 (redone)

def checkletters(x,y):
    if x=="A" and y=="T":
        return True
    elif x=="T" and y=="A":
        return True
    elif x=="G" and y=="C":
        return True
    elif x=="C" and y=="G":
        return True
    else:
        return False
def mismatched_pairs(string1,string2):
    if len(string1)!=len(string2):
        return string1+" and "+string2+" DNA strings do not have the same length."
    else:
        counter=0
        for index in range(len(string1)):
            if checkletters(string1[index],string2[index]) == False:
                counter=counter+1
        return counter

#Inspired by Question 2

def reversal(x):
    if x=="A":
        return "Z"
    elif x=="B":
        return "Y"
    elif x=="C":
        return "X"
    elif x=="D":
        return "W"
    elif x=="E":
        return "V"
    elif x=="F":
        return "U"
    elif x=="G":
        return "T"
    elif x=="H":
        return "S"
    elif x=="I":
        return "R"
    elif x=="J":
        return "Q"
    elif x=="K":
        return "P"
    elif x=="L":
        return "O"
    elif x=="M":
        return "N"
    elif x=="N":
        return "M"
    elif x=="O":
        return "L"
    elif x=="P":
        return "K"
    elif x=="Q":
        return "J"
    elif x=="R":
        return "I"
    elif x=="S":
        return "H"
    elif x=="T":
        return "G"
    elif x=="U":
        return "F"
    elif x=="V":
        return "E"
    elif x=="W":
        return "D"
    elif x=="X":
        return "C"
    elif x=="Y":
        return "B"
    elif x=="Z":
        return "A"
    elif x==" ":
        return " "
    else:
        return "Error: Incorrect character."

def secretcode(decoded):
    if decoded=="":
        return "Error: no input received."
    else:
        encoded=""
        for letter in decoded:
            encoded=encoded+reversal(letter)
        return encoded

#Question 3

def prime(x):
    if x==1:
        return False
    for number in range(2,x):
        if x%number==0:
            return False
        else:
            return True

def first_n_primes(n, mylist):
    if mylist==[]:
        return "Error: Empty list."
    else:
        finallist=[]
        for number in mylist:
            if prime(number) == True and len(finallist)<n:
                print number
                finallist.append(number)
        if len(finallist)==0:
            print "I didn't find any primes."
        elif len(finallist)<n:
            print "I only found "+str(len(finallist))+" primes."

#Question 4
#Review again

def combos(x):
    for numbers in range(1,x+1):
        print str(numbers)+" :"

def bands(list1,list2,list3,list4):
    band_number=1
    if list1==[]:
        return "We cannot form a band without a lead singer."
    elif list2==[]:
        return "We cannot form a band without a drummer."
    elif list3==[]:
        return "We cannot form a band without a bass player."
    elif list4==[]:
        return "We cannot form a band without a guitar player."
    else:
        for I in list1:
            for II in list2:
                for III in list3:
                    for IV in list4:
                        print str(band_number)+" :"+str(I)+","+str(II)+","+str(III)+","+str(IV)+","
                        band_number=band_number+1
