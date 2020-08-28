'''
Created on Feb 16, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''
def knapsack(capacity,itemList):
    if itemList == []:
        return [0,[]]
    elif capacity == 0:
        return [0,[]]
    else:
        firstitem = itemList[0]
        if capacity < firstitem[0]:
            return knapsack(capacity, itemList[1:])
        else:
            useItSetup = knapsack(capacity - firstitem[0],itemList[1:])
            useIt = [firstitem[1] + useItSetup[0], [firstitem] + useItSetup[1]]
            loseIt = knapsack(capacity,itemList[1:])
            if useIt[0] < loseIt[0]:
                return loseIt
            else:
                return useIt