'''
Created on Feb 16, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

def pascal_row(mynumber):
    '''This function returns a single list of the pascal triangle number sequence with n many numbers. If the number is zero,
       we will return a listified 1, and if it is one, we will return a list containing 1,1. If it is not, then we will use the
       pascal method for solving for the middle and include a 1 on each end of it.'''
    if mynumber == 0:
        return [1]
    elif mynumber == 1:
        return [1,1]
    else:
        return [1] + pascalAdd(pascal_row(mynumber-1),mynumber) + [1]

def pascalAdd(mylist,counter):
    '''Returns the sums in the pascal triangle to be put on the inside of the outer ones.
       Works by adding the first and second items until there are fewer than two items.'''
    if len(mylist) < 2:
        return []
    elif counter == 0:
        return []
    else:
        return [mylist[0] + mylist[1]] + pascalAdd(mylist[1:],counter-1)

def pascal_triangle(mynumber):
    '''This function returns the pascal triangle helper function, using mynumber as mynumber and counter as mynumber, as both the counter
       and the number have to equal zero at first.'''
    return pascalTriangleHelp(mynumber,mynumber)

def pascalTriangleHelp(mynumber,counter):
    '''Returns the list of pascal triangle sequences from 0 to n. This is necessary because if we use the parent function without the
       helper function, we will get the same list, but in descending order from n to 0.'''
    if counter == 0:
        return [pascal_row(mynumber)]
    else:
        return [pascal_row(mynumber-counter)] + pascalTriangleHelp(mynumber,counter-1)
