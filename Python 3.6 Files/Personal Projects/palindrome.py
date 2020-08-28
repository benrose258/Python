'''
Created on May 2, 2017

@author: Ben Rose
'''
import sys

class Stack(object):
    def __init__(self):
        self.__items = []
    
    def isEmpty(self):
        return self.__items == []
    
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[-1]
    
    def size(self):
        return len(self.__items)
    
def isPalindrome(mystring):
    mystring = mystring.lower()
    stack = Stack()
    for letter in mystring:
        stack.push(letter)
    for letter in mystring:
        if stack.pop() != letter:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + ' <string>')
        sys.exit(1)
    print('String: ' + sys.argv[1])
    print(isPalindrome(sys.argv[1]))
    sys.exit(0)
