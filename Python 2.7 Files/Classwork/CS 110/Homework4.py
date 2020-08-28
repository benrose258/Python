#Homework 4
#Question 1
def head(myList):
    if len(myList) == 0:
        print "Error: the empty list has no head"
    else:
        return myList[0]

#Question 2
def tail(myList):
    if len(myList) == 0:
        print "Error: the empty list has no tail"
    else:
        return myList[1:]

#Question 3
def replace_and_triple(x, y, z, myList):
    resultList = list()
    if x == z:
        return myList
    else:
        for number in myList:
            if number==x:
                resultList.append(y)
            elif number==z:
                resultList.append(3 * z)
            else:
                resultList.append(number)
        return resultList

'''For question 1, the "if" statement can be more effeciently written as:
   if myList == []:
       print "Error: the empty list has no head"
   else:
       return myList[0]
   Same goes for the second question.
   Also, [0] can be rewritten as [:1]'''
