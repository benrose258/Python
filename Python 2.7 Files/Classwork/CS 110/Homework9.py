#Question 1

def subset(target,mylist):
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

#Question 2

def LCS(string1,string2):
    if string1 == '' or string2 == '':
        return 0
    elif string1[0] == string2[0]:
        return 1 + LCS(string1[1:],string2[1:])
    else:
        option1 = LCS(string1,string2[1:])
        option2 = LCS(string1[1:],string2)
        return max(option1,option2)

#Question 3

def ED(string1,string2):
    if string1 == "":
        return len(string2)
    elif string2 == "":
        return len(string1)
    elif string1[0]==string2[0]:
        return ED(string1[1:],string2[1:])
    else:
        #substitute, insert, or delete!
        substitute = 1 + ED(string1[1:],string2[1:])
        insert = 1 + ED(string1,string2[1:])
        delete = 1 + ED(string1[1:],string2)
        return min(substitute,insert,delete)
