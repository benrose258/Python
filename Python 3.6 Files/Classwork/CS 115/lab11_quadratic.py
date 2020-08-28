'''
Created on Apr 20, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
import sys

class QuadraticEquation(object):
    
    def __init__(self,a,b,c):
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0:
            raise ValueError('Coefficient \'a\' cannot be 0 in a quadratic equation.')
            sys.exit(1)
        else:
            self.a = a
            self.b = b
            self.c = c
    
    def a(self):
        return self.a()
    
    def b(self):
        return self.b()
    
    def c(self):
        return self.c()
    
    def discriminant(self):
        return self.b**2 - 4*self.a*self.c
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + self.discriminant()**(1/2))/(2 * self.a)
    
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - self.discriminant()**(1/2))/(2 * self.a)
    
    def __str__(self):
        eqPartA = str(self.a)+'x^2 '
        eqPartB = '+ ' + str(abs(self.b)) + 'x '
        eqPartC = '+ ' + str(abs(self.c)) + ' '
        if self.a == -1:
            eqPartA = '-' + eqPartA[-4:]
        elif self.a == 1:
            eqPartA = eqPartA[-4:]
        if self.b == 0:
            eqPartB = ''
        elif self.b == 1:
            eqPartB = eqPartB[:2] + eqPartB[-2:]
        elif self.b == -1:
            eqPartB = '- ' + eqPartB[-2:]
        elif self.b < 0:
            eqPartB = '-' + eqPartB[1:]
        if self.c == 0:
            eqPartC = ''
        elif self.c < 0:
            eqPartC = '-' + eqPartC[1:]
        return eqPartA + eqPartB + eqPartC + '= 0'

q = QuadraticEquation(1,0.059,-0.0118)
print(q.root1())
print(q.root2())
