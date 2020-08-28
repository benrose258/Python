'''
Created on Feb 14, 2017

@author: Ben Rose
'''

'''LCS: Longest Common String'''

def LCS(string1,string2):
    if string1 == '' or string2 == '':
        return 0
    elif string1[0] == string2[0]:
        return 1 + LCS(string1[1:],string2[1:])
    else:
        useString1 = LCS(string1,string2[1:])
        useString2 = LCS(string1[1:],string2)
        return max(useString1,useString2)
