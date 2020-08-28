'''
Created on Apr 10, 2017

@author: Ben Rose
'''
import random
import time

def sequentialSearch(mylist,key):
    for index in range(len(mylist)):
        if mylist[index] == key:
            return index
    return -1

def binarySearch(mylist,key):
    low = 0
    high = len(mylist) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if mylist[mid] == key:
            return mid
        elif mylist[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -low - 1

lst = [random.randint(1,100000) for _ in range(1000000)]

def swap(mylist,i,j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp

# Selection sort always makes n(n-1)/2 comparisons.
# Therefore, selection sort makes at most n-1 swaps.

def selectionSort(mylist):
    n = len(mylist)
    for i in range(n-1):
        minIndex = i
        for j in range(i + 1, n):
            if mylist[j] < mylist[minIndex]:
                minIndex = j
        if i != minIndex:
            swap(mylist,i,minIndex)
