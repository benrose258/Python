def cypher():
    needinstructions = input("Would you like instructions? ")
    if needinstructions == Yes or needinstructions == yes:
        print ""
        print "Cypher works by first encrypting your message using the code you provide. You can stop the program any time by typing in Stop or stop and it will return your message."
        print ""
        print "The decypher method will be shown encrypted, only to be read using the provided code in reverse."
        print ""
    mymessage = input("Please input your message... ")
    return cypherbrain(mymessage)

def cypherbrain(mymessage):
    whatencryption = input("Please put in a number 0-9 to use as your code... ")
    if whatencryption == 0:
        mymessage = caesarencypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 1:
        mymessage = plusitselfencypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 2:
        mymessage = quertyencypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 3:
        mymessage = quickbrownfoxencypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 4:
        mymessage = squareitselfencypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 5:
        mymessage = caesardecypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 6:
        mymessage = plusitselfdecypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 7:
        mymessage = quertydecypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 8:
        mymessage = quickbrownfoxdecypher(mymessage)
        return cypherbrain(mymessage)
    elif whatencryption == 9:
        mymessage = squareitselfdecypher(mymessage)
        return cypherbrain(mymessage)
    else:
        print ""
        print mymessage
        print ""
        return "Thank you for using Cypher. Your cypher text is above."
    print ""
    keepgoing = input("Would you like to restart cypher with your current message?")
    if keepgoing == Yes or keepgoing == yes or keepgoing == a or keepgoing == b or keepgoing == c or keepgoing == d or keepgoing == e or keepgoing == f or keepgoing == g or keepgoing == h or keepgoing == i or keepgoing == j or keepgoing == k or keepgoing == l or keepgoing == m or keepgoing == n or keepgoing == o or keepgoing == p or keepgoing == q or keepgoing == r or keepgoing == s or keepgoing == t or keepgoing == u or keepgoing == v or keepgoing == w or keepgoing == x or keepgoing == y or keepgoing == z:
        return cypherbrain(mymessage)
    else:
        print mymessage
        return "Thank you for using Cypher. Your cypher text is above."

def yes():
    return

def no():
    return

def Yes():
    return

def No():
    return

def a():
    return

def b():
    return

def c():
    return

def d():
    return

def e():
    return

def f():
    return

def g():
    return

def h():
    return

def i():
    return

def j():
    return

def k():
    return

def l():
    return

def m():
    return

def n():
    return

def o():
    return

def p():
    return

def q():
    return

def r():
    return

def s():
    return

def t():
    return

def u():
    return

def v():
    return

def w():
    return

def x():
    return

def y():
    return

def z():
    return

def quertyencypherkey(letter):
    if letter == "A":
        return "Q"
    elif letter == "B":
        return "W"
    elif letter == "C":
        return "E"
    elif letter == "D":
        return "R"
    elif letter == "E":
        return "T"
    elif letter == "F":
        return "Y"
    elif letter == "G":
        return "U"
    elif letter == "H":
        return "I"
    elif letter == "I":
        return "O"
    elif letter == "J":
        return "P"
    elif letter == "K":
        return "A"
    elif letter == "L":
        return "S"
    elif letter == "M":
        return "D"
    elif letter == "N":
        return "F"
    elif letter == "O":
        return "G"
    elif letter == "P":
        return "H"
    elif letter == "Q":
        return "J"
    elif letter == "R":
        return "K"
    elif letter == "S":
        return "L"
    elif letter == "T":
        return "Z"
    elif letter == "U":
        return "X"
    elif letter == "V":
        return "C"
    elif letter == "W":
        return "V"
    elif letter == "X":
        return "B"
    elif letter == "Y":
        return "N"
    elif letter == "Z":
        return "M"
    elif letter == "a":
        return "q"
    elif letter == "b":
        return "w"
    elif letter == "c":
        return "e"
    elif letter == "d":
        return "r"
    elif letter == "e":
        return "t"
    elif letter == "f":
        return "y"
    elif letter == "g":
        return "u"
    elif letter == "h":
        return "i"
    elif letter == "i":
        return "o"
    elif letter == "j":
        return "p"
    elif letter == "k":
        return "a"
    elif letter == "l":
        return "s"
    elif letter == "m":
        return "d"
    elif letter == "n":
        return "f"
    elif letter == "o":
        return "g"
    elif letter == "p":
        return "h"
    elif letter == "q":
        return "j"
    elif letter == "r":
        return "k"
    elif letter == "s":
        return "l"
    elif letter == "t":
        return "z"
    elif letter == "u":
        return "x"
    elif letter == "v":
        return "c"
    elif letter == "w":
        return "v"
    elif letter == "x":
        return "b"
    elif letter == "y":
        return "n"
    elif letter == "z":
        return "m"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def quertydecypherkey(letter):
    if letter == "A":
        return "K"
    elif letter == "B":
        return "X"
    elif letter == "C":
        return "V"
    elif letter == "D":
        return "M"
    elif letter == "E":
        return "C"
    elif letter == "F":
        return "N"
    elif letter == "G":
        return "O"
    elif letter == "H":
        return "P"
    elif letter == "I":
        return "H"
    elif letter == "J":
        return "Q"
    elif letter == "K":
        return "R"
    elif letter == "L":
        return "S"
    elif letter == "M":
        return "Z"
    elif letter == "N":
        return "Y"
    elif letter == "O":
        return "I"
    elif letter == "P":
        return "J"
    elif letter == "Q":
        return "A"
    elif letter == "R":
        return "D"
    elif letter == "S":
        return "L"
    elif letter == "T":
        return "E"
    elif letter == "U":
        return "G"
    elif letter == "V":
        return "W"
    elif letter == "W":
        return "B"
    elif letter == "X":
        return "U"
    elif letter == "Y":
        return "F"
    elif letter == "Z":
        return "T"
    elif letter == "a":
        return "k"
    elif letter == "b":
        return "x"
    elif letter == "c":
        return "v"
    elif letter == "d":
        return "m"
    elif letter == "e":
        return "c"
    elif letter == "f":
        return "n"
    elif letter == "g":
        return "o"
    elif letter == "h":
        return "p"
    elif letter == "i":
        return "h"
    elif letter == "j":
        return "q"
    elif letter == "k":
        return "r"
    elif letter == "l":
        return "s"
    elif letter == "m":
        return "z"
    elif letter == "n":
        return "y"
    elif letter == "o":
        return "i"
    elif letter == "p":
        return "j"
    elif letter == "q":
        return "a"
    elif letter == "r":
        return "d"
    elif letter == "s":
        return "l"
    elif letter == "t":
        return "e"
    elif letter == "u":
        return "g"
    elif letter == "v":
        return "w"
    elif letter == "w":
        return "b"
    elif letter == "x":
        return "u"
    elif letter == "y":
        return "f"
    elif letter == "z":
        return "t"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def quertyencypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            return "Error: Incorrect character. Please try again."
        else:
            finalstring = finalstring + quertyencypherkey(letter)
    return finalstring

def quertydecypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            return "Error: Incorrect character. Please try again."
        else:
            finalstring = finalstring + quertydecypherkey(letter)
    return finalstring

def quickbrownfoxencypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Incorrect character. Please try again."
            return finalstring
        else:
            finalstring = finalstring + quickbrownfoxencypherkey(letter)
    return finalstring

def quickbrownfoxdecypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Incorrect character. Please try again."
            return finalstring
        else:
            finalstring = finalstring + quickbrownfoxdecypherkey(letter)
    return finalstring

def quickbrownfoxencypherkey(letter):
    if letter == "A":
        return "T"
    elif letter == "B":
        return "H"
    elif letter == "C":
        return "E"
    elif letter == "D":
        return "Q"
    elif letter == "E":
        return "U"
    elif letter == "F":
        return "I"
    elif letter == "G":
        return "C"
    elif letter == "H":
        return "K"
    elif letter == "I":
        return "B"
    elif letter == "J":
        return "R"
    elif letter == "K":
        return "O"
    elif letter == "L":
        return "W"
    elif letter == "M":
        return "N"
    elif letter == "N":
        return "F"
    elif letter == "O":
        return "X"
    elif letter == "P":
        return "J"
    elif letter == "Q":
        return "M"
    elif letter == "R":
        return "P"
    elif letter == "S":
        return "S"
    elif letter == "T":
        return "V"
    elif letter == "U":
        return "L"
    elif letter == "V":
        return "A"
    elif letter == "W":
        return "Z"
    elif letter == "X":
        return "Y"
    elif letter == "Y":
        return "D"
    elif letter == "Z":
        return "G"
    elif letter == "a":
        return "t"
    elif letter == "b":
        return "h"
    elif letter == "c":
        return "e"
    elif letter == "d":
        return "q"
    elif letter == "e":
        return "u"
    elif letter == "f":
        return "i"
    elif letter == "g":
        return "c"
    elif letter == "h":
        return "k"
    elif letter == "i":
        return "b"
    elif letter == "j":
        return "r"
    elif letter == "k":
        return "o"
    elif letter == "l":
        return "w"
    elif letter == "m":
        return "n"
    elif letter == "n":
        return "f"
    elif letter == "o":
        return "x"
    elif letter == "p":
        return "j"
    elif letter == "q":
        return "m"
    elif letter == "r":
        return "p"
    elif letter == "s":
        return "s"
    elif letter == "t":
        return "v"
    elif letter == "u":
        return "l"
    elif letter == "v":
        return "a"
    elif letter == "w":
        return "z"
    elif letter == "x":
        return "y"
    elif letter == "y":
        return "d"
    elif letter == "z":
        return "g"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def quickbrownfoxdecypherkey(letter):
    if letter == "A":
        return "V"
    elif letter == "B":
        return "I"
    elif letter == "C":
        return "G"
    elif letter == "D":
        return "Y"
    elif letter == "E":
        return "C"
    elif letter == "F":
        return "N"
    elif letter == "G":
        return "Z"
    elif letter == "H":
        return "B"
    elif letter == "I":
        return "F"
    elif letter == "J":
        return "P"
    elif letter == "K":
        return "H"
    elif letter == "L":
        return "U"
    elif letter == "M":
        return "Q"
    elif letter == "N":
        return "M"
    elif letter == "O":
        return "K"
    elif letter == "P":
        return "R"
    elif letter == "Q":
        return "D"
    elif letter == "R":
        return "J"
    elif letter == "S":
        return "S"
    elif letter == "T":
        return "A"
    elif letter == "U":
        return "E"
    elif letter == "V":
        return "T"
    elif letter == "W":
        return "L"
    elif letter == "X":
        return "O"
    elif letter == "Y":
        return "X"
    elif letter == "Z":
        return "W"
    elif letter == "a":
        return "v"
    elif letter == "b":
        return "i"
    elif letter == "c":
        return "g"
    elif letter == "d":
        return "y"
    elif letter == "e":
        return "c"
    elif letter == "f":
        return "n"
    elif letter == "g":
        return "z"
    elif letter == "h":
        return "b"
    elif letter == "i":
        return "f"
    elif letter == "j":
        return "p"
    elif letter == "k":
        return "h"
    elif letter == "l":
        return "u"
    elif letter == "m":
        return "q"
    elif letter == "n":
        return "m"
    elif letter == "o":
        return "k"
    elif letter == "p":
        return "r"
    elif letter == "q":
        return "d"
    elif letter == "r":
        return "j"
    elif letter == "s":
        return "s"
    elif letter == "t":
        return "a"
    elif letter == "u":
        return "e"
    elif letter == "v":
        return "t"
    elif letter == "w":
        return "l"
    elif letter == "x":
        return "o"
    elif letter == "y":
        return "x"
    elif letter == "z":
        return "w"
    elif letter == "1":
        return "1"
    elif letter == "2":
        return "2"
    elif letter == "3":
        return "3"
    elif letter == "4":
        return "4"
    elif letter == "5":
        return "5"
    elif letter == "6":
        return "6"
    elif letter == "7":
        return "7"
    elif letter == "8":
        return "8"
    elif letter == "9":
        return "9"
    elif letter == "0":
        return "0"
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def squareitselfencypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Incorrect character. Please try again."
            return finalstring
        else:
            finalstring = finalstring + squareitselfencypherkey(letter)
    return finalstring

def squareitselfdecypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Incorrect character. Please try again."
            return finalstring
        else:
            finalstring = finalstring + squareitselfdecypherkey(letter)
    return finalstring

def squareitselfencypherkey(letter):
    if letter == "A":
        return "A"
    elif letter == "B":
        return "D"
    elif letter == "C":
        return "I"
    elif letter == "D":
        return "P"
    elif letter == "E":
        return "Y"
    elif letter == "F":
        return "J"
    elif letter == "G":
        return "W"
    elif letter == "H":
        return "L"
    elif letter == "I":
        return "C"
    elif letter == "J":
        return "V"
    elif letter == "K":
        return "Q"
    elif letter == "L":
        return "N"
    elif letter == "M":
        return "M"
    elif letter == "N":
        return "O"
    elif letter == "O":
        return "R"
    elif letter == "P":
        return "X"
    elif letter == "Q":
        return "E"
    elif letter == "R":
        return "S"
    elif letter == "S":
        return "Z"
    elif letter == "T":
        return "K"
    elif letter == "U":
        return "B"
    elif letter == "V":
        return "T"
    elif letter == "W":
        return "U"
    elif letter == "X":
        return "F"
    elif letter == "Y":
        return "G"
    elif letter == "Z":
        return "H"
    elif letter == "a":
        return "a"
    elif letter == "b":
        return "d"
    elif letter == "c":
        return "i"
    elif letter == "d":
        return "p"
    elif letter == "e":
        return "y"
    elif letter == "f":
        return "j"
    elif letter == "g":
        return "w"
    elif letter == "h":
        return "l"
    elif letter == "i":
        return "c"
    elif letter == "j":
        return "v"
    elif letter == "k":
        return "q"
    elif letter == "l":
        return "n"
    elif letter == "m":
        return "m"
    elif letter == "n":
        return "o"
    elif letter == "o":
        return "r"
    elif letter == "p":
        return "x"
    elif letter == "q":
        return "e"
    elif letter == "r":
        return "s"
    elif letter == "s":
        return "z"
    elif letter == "t":
        return "k"
    elif letter == "u":
        return "b"
    elif letter == "v":
        return "t"
    elif letter == "w":
        return "u"
    elif letter == "x":
        return "f"
    elif letter == "y":
        return "g"
    elif letter == "z":
        return "h"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def squareitselfdecypherkey(letter):
    if letter == "A":
        return "A"
    elif letter == "B":
        return "U"
    elif letter == "C":
        return "I"
    elif letter == "D":
        return "B"
    elif letter == "E":
        return "Q"
    elif letter == "F":
        return "X"
    elif letter == "G":
        return "Y"
    elif letter == "H":
        return "Z"
    elif letter == "I":
        return "C"
    elif letter == "J":
        return "F"
    elif letter == "K":
        return "T"
    elif letter == "L":
        return "H"
    elif letter == "M":
        return "M"
    elif letter == "N":
        return "L"
    elif letter == "O":
        return "N"
    elif letter == "P":
        return "D"
    elif letter == "Q":
        return "K"
    elif letter == "R":
        return "O"
    elif letter == "S":
        return "R"
    elif letter == "T":
        return "V"
    elif letter == "U":
        return "W"
    elif letter == "V":
        return "J"
    elif letter == "W":
        return "G"
    elif letter == "X":
        return "P"
    elif letter == "Y":
        return "E"
    elif letter == "Z":
        return "S"
    elif letter == "a":
        return "a"
    elif letter == "b":
        return "u"
    elif letter == "c":
        return "i"
    elif letter == "d":
        return "b"
    elif letter == "e":
        return "q"
    elif letter == "f":
        return "x"
    elif letter == "g":
        return "y"
    elif letter == "h":
        return "z"
    elif letter == "i":
        return "c"
    elif letter == "j":
        return "f"
    elif letter == "k":
        return "t"
    elif letter == "l":
        return "h"
    elif letter == "m":
        return "m"
    elif letter == "n":
        return "l"
    elif letter == "o":
        return "n"
    elif letter == "p":
        return "d"
    elif letter == "q":
        return "k"
    elif letter == "r":
        return "o"
    elif letter == "s":
        return "r"
    elif letter == "t":
        return "v"
    elif letter == "u":
        return "w"
    elif letter == "v":
        return "j"
    elif letter == "w":
        return "g"
    elif letter == "x":
        return "p"
    elif letter == "y":
        return "e"
    elif letter == "z":
        return "s"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def CaesarEncypherHelp(letter):
    if letter == "A":
        return "D"
    elif letter == "B":
        return "E"
    elif letter == "C":
        return "F"
    elif letter == "D":
        return "G"
    elif letter == "E":
        return "H"
    elif letter == "F":
        return "I"
    elif letter == "G":
        return "J"
    elif letter == "H":
        return "K"
    elif letter == "I":
        return "L"
    elif letter == "J":
        return "M"
    elif letter == "K":
        return "N"
    elif letter == "L":
        return "O"
    elif letter == "M":
        return "P"
    elif letter == "N":
        return "Q"
    elif letter == "O":
        return "R"
    elif letter == "P":
        return "S"
    elif letter == "Q":
        return "T"
    elif letter == "R":
        return "U"
    elif letter == "S":
        return "V"
    elif letter == "T":
        return "W"
    elif letter == "U":
        return "X"
    elif letter == "V":
        return "Y"
    elif letter == "W":
        return "Z"
    elif letter == "X":
        return "A"
    elif letter == "Y":
        return "B"
    elif letter == "Z":
        return "C"
    elif letter == "a":
        return "d"
    elif letter == "b":
        return "e"
    elif letter == "c":
        return "f"
    elif letter == "d":
        return "g"
    elif letter == "e":
        return "h"
    elif letter == "f":
        return "i"
    elif letter == "g":
        return "j"
    elif letter == "h":
        return "k"
    elif letter == "i":
        return "l"
    elif letter == "j":
        return "m"
    elif letter == "k":
        return "n"
    elif letter == "l":
        return "o"
    elif letter == "m":
        return "p"
    elif letter == "n":
        return "q"
    elif letter == "o":
        return "r"
    elif letter == "p":
        return "s"
    elif letter == "q":
        return "t"
    elif letter == "r":
        return "u"
    elif letter == "s":
        return "v"
    elif letter == "t":
        return "w"
    elif letter == "u":
        return "x"
    elif letter == "v":
        return "y"
    elif letter == "w":
        return "z"
    elif letter == "x":
        return "a"
    elif letter == "y":
        return "b"
    elif letter == "z":
        return "c"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def caesarencypher(message):
    encoded = ""
    for letter in message:
        if CaesarEncypherHelp(letter)=="Error":
            encoded = "Error: Incorrect character. Please try again."
            return encoded
        else:
            encoded=encoded+CaesarEncypherHelp(letter)
    return encoded

def CaesarDecypherHelp(letter):
    if letter == "A":
        return "X"
    elif letter == "B":
        return "Y"
    elif letter == "C":
        return "Z"
    elif letter == "D":
        return "A"
    elif letter == "E":
        return "B"
    elif letter == "F":
        return "C"
    elif letter == "G":
        return "D"
    elif letter == "H":
        return "E"
    elif letter == "I":
        return "F"
    elif letter == "J":
        return "G"
    elif letter == "K":
        return "H"
    elif letter == "L":
        return "I"
    elif letter == "M":
        return "J"
    elif letter == "N":
        return "K"
    elif letter == "O":
        return "L"
    elif letter == "P":
        return "M"
    elif letter == "Q":
        return "N"
    elif letter == "R":
        return "O"
    elif letter == "S":
        return "P"
    elif letter == "T":
        return "Q"
    elif letter == "U":
        return "R"
    elif letter == "V":
        return "S"
    elif letter == "W":
        return "T"
    elif letter == "X":
        return "U"
    elif letter == "Y":
        return "V"
    elif letter == "Z":
        return "W"
    elif letter == "a":
        return "x"
    elif letter == "b":
        return "y"
    elif letter == "c":
        return "z"
    elif letter == "d":
        return "a"
    elif letter == "e":
        return "b"
    elif letter == "f":
        return "c"
    elif letter == "g":
        return "d"
    elif letter == "h":
        return "e"
    elif letter == "i":
        return "f"
    elif letter == "j":
        return "g"
    elif letter == "k":
        return "h"
    elif letter == "l":
        return "i"
    elif letter == "m":
        return "j"
    elif letter == "n":
        return "k"
    elif letter == "o":
        return "l"
    elif letter == "p":
        return "m"
    elif letter == "q":
        return "n"
    elif letter == "r":
        return "o"
    elif letter == "s":
        return "p"
    elif letter == "t":
        return "q"
    elif letter == "u":
        return "r"
    elif letter == "v":
        return "s"
    elif letter == "w":
        return "t"
    elif letter == "x":
        return "u"
    elif letter == "y":
        return "v"
    elif letter == "z":
        return "w"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def caesardecypher(message):
    decyphered = ""
    for letter in message:
        if CaesarDecypherHelp(letter)=="Error":
            decyphered = "Error: Incorrect character. Please try again."
            return decyphered
        else:
            decyphered = decyphered + CaesarDecypherHelp(letter)
    return decyphered

def plusitselfencypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Incorrect character. Please try again."
            return finalstring
        else:
            finalstring = finalstring + plusitselfencypherkey(letter)
    return finalstring

def plusitselfdecypher(mymessage):
    finalstring = ''
    for letter in mymessage:
         if letter == "Error":
             finalstring = "Error: Incorrect character. Please try again."
             return finalstring
         else:
             finalstring = finalstring + plusitselfdecypherkey(letter)
    return finalstring

def plusitselfencypherkey(letter):
    if letter == "A":
        return "B"
    elif letter == "B":
        return "D"
    elif letter == "C":
        return "F"
    elif letter == "D":
        return "H"
    elif letter == "E":
        return "J"
    elif letter == "F":
        return "L"
    elif letter == "G":
        return "N"
    elif letter == "H":
        return "P"
    elif letter == "I":
        return "R"
    elif letter == "J":
        return "T"
    elif letter == "K":
        return "V"
    elif letter == "L":
        return "X"
    elif letter == "M":
        return "Z"
    elif letter == "N":
        return "A"
    elif letter == "O":
        return "C"
    elif letter == "P":
        return "E"
    elif letter == "Q":
        return "G"
    elif letter == "R":
        return "I"
    elif letter == "S":
        return "K"
    elif letter == "T":
        return "M"
    elif letter == "U":
        return "O"
    elif letter == "V":
        return "Q"
    elif letter == "W":
        return "S"
    elif letter == "X":
        return "U"
    elif letter == "Y":
        return "W"
    elif letter == "Z":
        return "Y"
    elif letter == "a":
        return "b"
    elif letter == "b":
        return "d"
    elif letter == "c":
        return "f"
    elif letter == "d":
        return "h"
    elif letter == "e":
        return "j"
    elif letter == "f":
        return "l"
    elif letter == "g":
        return "n"
    elif letter == "h":
        return "p"
    elif letter == "i":
        return "r"
    elif letter == "j":
        return "t"
    elif letter == "k":
        return "v"
    elif letter == "l":
        return "x"
    elif letter == "m":
        return "z"
    elif letter == "n":
        return "a"
    elif letter == "o":
        return "c"
    elif letter == "p":
        return "e"
    elif letter == "q":
        return "g"
    elif letter == "r":
        return "i"
    elif letter == "s":
        return "k"
    elif letter == "t":
        return "m"
    elif letter == "u":
        return "o"
    elif letter == "v":
        return "q"
    elif letter == "w":
        return "s"
    elif letter == "x":
        return "u"
    elif letter == "y":
        return "w"
    elif letter == "z":
        return "y"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"

def plusitselfdecypherkey(letter):
    if letter == "A":
        return "N"
    elif letter == "B":
        return "A"
    elif letter == "C":
        return "O"
    elif letter == "D":
        return "B"
    elif letter == "E":
        return "P"
    elif letter == "F":
        return "C"
    elif letter == "G":
        return "Q"
    elif letter == "H":
        return "D"
    elif letter == "I":
        return "R"
    elif letter == "J":
        return "E"
    elif letter == "K":
        return "S"
    elif letter == "L":
        return "F"
    elif letter == "M":
        return "T"
    elif letter == "N":
        return "G"
    elif letter == "O":
        return "U"
    elif letter == "P":
        return "H"
    elif letter == "Q":
        return "V"
    elif letter == "R":
        return "I"
    elif letter == "S":
        return "W"
    elif letter == "T":
        return "J"
    elif letter == "U":
        return "X"
    elif letter == "V":
        return "K"
    elif letter == "W":
        return "Y"
    elif letter == "X":
        return "L"
    elif letter == "Y":
        return "Z"
    elif letter == "Z":
        return "M"
    elif letter == "a":
        return "n"
    elif letter == "b":
        return "a"
    elif letter == "c":
        return "o"
    elif letter == "d":
        return "b"
    elif letter == "e":
        return "p"
    elif letter == "f":
        return "c"
    elif letter == "g":
        return "q"
    elif letter == "h":
        return "d"
    elif letter == "i":
        return "r"
    elif letter == "j":
        return "e"
    elif letter == "k":
        return "s"
    elif letter == "l":
        return "f"
    elif letter == "m":
        return "t"
    elif letter == "n":
        return "g"
    elif letter == "o":
        return "u"
    elif letter == "p":
        return "h"
    elif letter == "q":
        return "v"
    elif letter == "r":
        return "i"
    elif letter == "s":
        return "w"
    elif letter == "t":
        return "j"
    elif letter == "u":
        return "x"
    elif letter == "v":
        return "k"
    elif letter == "w":
        return "y"
    elif letter == "x":
        return "l"
    elif letter == "y":
        return "z"
    elif letter == "z":
        return "m"
    elif letter == '1':
        return '1'
    elif letter == '2':
        return '2'
    elif letter == '3':
        return '3'
    elif letter == '4':
        return '4'
    elif letter == '5':
        return '5'
    elif letter == '6':
        return '6'
    elif letter == '7':
        return '7'
    elif letter == '8':
        return '8'
    elif letter == '9':
        return '9'
    elif letter == '0':
        return '0'
    elif letter == " ":
        return " "
    elif letter == "!":
        return "!"
    elif letter == "?":
        return "?"
    elif letter == ".":
        return "."
    elif letter == ",":
        return ","
    elif letter == "%":
        return "%"
    else:
        return "Error"
