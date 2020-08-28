#Keyboard Cypher
def keyboardcypher():
    encryptordecrypt = input("Would you like to encode or decode a message? ")
    if encryptordecrypt == "encode" or encryptordecrypt == "Encode":
        askformessage = input("What message would you like encoded? ")
        return quertyencypher(askformessage)
    elif encryptordecrypt == "decode" or "Decode":
        askforencryptedmessage = input("What message would you like decoded? ")
        return quertydecypher(askforencryptedmessage)
    else:
        print "Error: Incorrect character. Please try again."
        return keyboardcypher()

def quertyencypher(mystring):
    finalstring = ""
    for letter in mystring:
        if letter == "A":
            finalstring = finalstring + "Q"
        elif letter == "B":
            finalstring = finalstring + "U"
        elif letter == "C":
            finalstring = finalstring + "E"
        elif letter == "D":
            finalstring = finalstring + "R"
        elif letter == "E":
            finalstring = finalstring + "T"
        elif letter == "F":
            finalstring = finalstring + "Y"
        elif letter == "G":
            finalstring = finalstring + "U"
        elif letter == "H":
            finalstring = finalstring + "I"
        elif letter == "I":
            finalstring = finalstring + "O"
        elif letter == "J":
            finalstring = finalstring + "P"
        elif letter == "K":
            finalstring = finalstring + "A"
        elif letter == "L":
            finalstring = finalstring + "S"
        elif letter == "M":
            finalstring = finalstring + "D"
        elif letter == "N":
            finalstring = finalstring + "F"
        elif letter == "O":
            finalstring = finalstring + "G"
        elif letter == "P":
            finalstring = finalstring + "H"
        elif letter == "Q":
            finalstring = finalstring + "J"
        elif letter == "R":
            finalstring = finalstring + "K"
        elif letter == "S":
            finalstring = finalstring + "L"
        elif letter == "T":
            finalstring = finalstring + "Z"
        elif letter == "U":
            finalstring = finalstring + "X"
        elif letter == "V":
            finalstring = finalstring + "C"
        elif letter == "W":
            finalstring = finalstring + "V"
        elif letter == "X":
            finalstring = finalstring + "B"
        elif letter == "Y":
            finalstring = finalstring + "N"
        elif letter == "Z":
            finalstring = finalstring + "M"
        elif letter == "a":
            finalstring = finalstring + "q"
        elif letter == "b":
            finalstring = finalstring + "w"
        elif letter == "c":
            finalstring = finalstring + "e"
        elif letter == "d":
            finalstring = finalstring + "r"
        elif letter == "e":
            finalstring = finalstring + "t"
        elif letter == "f":
            finalstring = finalstring + "y"
        elif letter == "g":
            finalstring = finalstring + "u"
        elif letter == "h":
            finalstring = finalstring + "i"
        elif letter == "i":
            finalstring = finalstring + "o"
        elif letter == "j":
            finalstring = finalstring + "p"
        elif letter == "k":
            finalstring = finalstring + "a"
        elif letter == "l":
            finalstring = finalstring + "s"
        elif letter == "m":
            finalstring = finalstring + "d"
        elif letter == "n":
            finalstring = finalstring + "f"
        elif letter == "o":
            finalstring = finalstring + "g"
        elif letter == "p":
            finalstring = finalstring + "h"
        elif letter == "q":
            finalstring = finalstring + "j"
        elif letter == "r":
            finalstring = finalstring + "k"
        elif letter == "s":
            finalstring = finalstring + "l"
        elif letter == "t":
            finalstring = finalstring + "z"
        elif letter == "u":
            finalstring = finalstring + "x"
        elif letter == "v":
            finalstring = finalstring + "c"
        elif letter == "w":
            finalstring = finalstring + "v"
        elif letter == "x":
            finalstring = finalstring + "b"
        elif letter == "y":
            finalstring = finalstring + "n"
        elif letter == "z":
            finalstring = finalstring + "m"
        elif letter == " ":
            finalstring = finalstring + " "
        elif letter == "!":
            finalstring = finalstring + "!"
        elif letter == "?":
            finalstring = finalstring + "?"
        elif letter == ".":
            finalstring = finalstring + "."
        elif letter == ",":
            finalstring = finalstring + ","
        else:
            finalstring = "%%%%%"
    if finalstring == "%%%%%":
        return "Error: Incorrect character. Please try again."
    else:
        return finalstring

def quertydecypher(mystring):
    finalstring = ""
    for letter in mystring:
        if letter == "Q":
            finalstring = finalstring + "A"
        elif letter == "W":
            finalstring = finalstring + "B"
        elif letter == "E":
            finalstring = finalstring + "C"
        elif letter == "R":
            finalstring = finalstring + "D"
        elif letter == "T":
            finalstring = finalstring + "E"
        elif letter == "Y":
            finalstring = finalstring + "F"
        elif letter == "U":
            finalstring = finalstring + "G"
        elif letter == "I":
            finalstring = finalstring + "H"
        elif letter == "O":
            finalstring = finalstring + "I"
        elif letter == "P":
            finalstring = finalstring + "J"
        elif letter == "A":
            finalstring = finalstring + "K"
        elif letter == "S":
            finalstring = finalstring + "L"
        elif letter == "D":
            finalstring = finalstring + "M"
        elif letter == "F":
            finalstring = finalstring + "N"
        elif letter == "G":
            finalstring = finalstring + "O"
        elif letter == "H":
            finalstring = finalstring + "P"
        elif letter == "J":
            finalstring = finalstring + "Q"
        elif letter == "K":
            finalstring = finalstring + "R"
        elif letter == "L":
            finalstring = finalstring + "S"
        elif letter == "Z":
            finalstring = finalstring + "T"
        elif letter == "X":
            finalstring = finalstring + "U"
        elif letter == "C":
            finalstring = finalstring + "V"
        elif letter == "V":
            finalstring = finalstring + "W"
        elif letter == "B":
            finalstring = finalstring + "X"
        elif letter == "N":
            finalstring = finalstring + "Y"
        elif letter == "M":
            finalstring = finalstring + "Z"
        elif letter == "q":
            finalstring = finalstring + "a"
        elif letter == "w":
            finalstring = finalstring + "b"
        elif letter == "e":
            finalstring = finalstring + "c"
        elif letter == "r":
            finalstring = finalstring + "d"
        elif letter == "t":
            finalstring = finalstring + "e"
        elif letter == "y":
            finalstring = finalstring + "f"
        elif letter == "u":
            finalstring = finalstring + "g"
        elif letter == "i":
            finalstring = finalstring + "h"
        elif letter == "o":
            finalstring = finalstring + "i"
        elif letter == "p":
            finalstring = finalstring + "j"
        elif letter == "a":
            finalstring = finalstring + "k"
        elif letter == "s":
            finalstring = finalstring + "l"
        elif letter == "d":
            finalstring = finalstring + "m"
        elif letter == "f":
            finalstring = finalstring + "n"
        elif letter == "g":
            finalstring = finalstring + "o"
        elif letter == "h":
            finalstring = finalstring + "p"
        elif letter == "j":
            finalstring = finalstring + "q"
        elif letter == "k":
            finalstring = finalstring + "r"
        elif letter == "l":
            finalstring = finalstring + "s"
        elif letter == "z":
            finalstring = finalstring + "t"
        elif letter == "x":
            finalstring = finalstring + "u"
        elif letter == "c":
            finalstring = finalstring + "v"
        elif letter == "v":
            finalstring = finalstring + "w"
        elif letter == "b":
            finalstring = finalstring + "x"
        elif letter == "n":
            finalstring = finalstring + "y"
        elif letter == "m":
            finalstring = finalstring + "z"
        elif letter == " ":
            finalstring = finalstring + " "
        elif letter == "!":
            finalstring = finalstring + "!"
        elif letter == "?":
            finalstring = finalstring + "?"
        elif letter == ".":
            finalstring = finalstring + "."
        elif letter == ",":
            finalstring = finalstring + ","
        else:
            finalstring = "%%%%%"
    if finalstring == "%%%%%":
        return "Error: Incorrect character. Please try again."
    else:
        return finalstring
