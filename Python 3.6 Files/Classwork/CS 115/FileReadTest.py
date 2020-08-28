'''
Created on Mar 22, 2017

@author: Ben Rose
'''

def fileTest():
    words = []
    f = open('3esl.txt')
    for word in f:
        words.append(word)
    f.close
    for index in words:
        print (index)

print(fileTest())
