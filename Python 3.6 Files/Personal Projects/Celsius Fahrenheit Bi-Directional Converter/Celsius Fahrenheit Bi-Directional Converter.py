'''
Created on Jan 23, 2017

@author: Ben
'''

def FtoC(number):
    """Returns the input Fahrenheit in Celsius."""
    return (number-32)*5/9

def CtoF(number):
    """Returns the input Celsius degrees in Fahrenheit."""
    return (number*9/5)+32

def CelsiusAndFahrenheit():
    whichway = int(input("Would you like to convert from Fahrenheit to Celsius (a) or Celsius to Fahrenheit (b)? "))
    if whichway == a:
        whatnumber = int(input("Please input your temperature in Fahrenheit to be converted to Celsius... "))
        return FtoC(whatnumber)
    elif whichway == b:
        whatnumber = int(input("Please input your temperature in Celsius to be converted to Fahrenheit... "))
        return CtoF(whatnumber)
    else:
        return ("You have entered an incorrect character. Please try again.")

whichway = input("Would you like to convert from Fahrenheit to Celsius (a) or Celsius to Fahrenheit (b)? ")
    if whichway == 1:
        whatnumber = input("Please input your temperature in Fahrenheit to be converted to Celsius... ")
        return FtoC(whatnumber)
    elif whichway == 2:
        whatnumber = input("Please input your temperature in Celsius to be converted to Fahrenheit... ")
        return CtoF(whatnumber)
    else:
        return ("You have entered an incorrect character. Please try again.")

print (CtoF(50))
