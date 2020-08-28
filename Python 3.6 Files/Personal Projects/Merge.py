'''
Created on Apr 6, 2017

@author: Ben Rose
'''
list1 = ['A','C','D','F']
list2 = ['E','C','B','A']

def numMatches(list1,list2):
    '''Returns the number of elements that are in both list1 and list2'''
    list1.sort()
    list2.sort()
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

print(numMatches(list1,list2))

def keepMatches(list1,list2):
    '''Returns the list of elements that are in both list1 and list2'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

print(keepMatches(list1,list2))

def dropMatches(list1,list2):
    '''Returns the number of elements that are not in both list1 and list2'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

print(dropMatches(list1,list2))