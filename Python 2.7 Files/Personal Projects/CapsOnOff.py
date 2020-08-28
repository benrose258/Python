def caps(myletter):
    for letter in myletter:
        if letter == "A":
            return "A"
        elif letter == "B":
            return "B"
        elif letter == "C":
            return "C"
        elif letter == "D":
            return "D"
        elif letter == "E":
            return "E"
        elif letter == "F":
            return "F"
        elif letter == "G":
            return "G"
        elif letter == "H":
            return "H"
        elif letter == "I":
            return "I"
        elif letter == "J":
            return "J"
        elif letter == "K":
            return "K"
        elif letter == "L":
            return "L"
        elif letter == "M":
            return "M"
        elif letter == "N":
            return "N"
        elif letter == "O":
            return "O"
        elif letter == "P":
            return "P"
        elif letter == "Q":
            return "Q"
        elif letter == "R":
            return "R"
        elif letter == "S":
            return "S"
        elif letter == "T":
            return "T"
        elif letter == "U":
            return "U"
        elif letter == "V":
            return "V"
        elif letter == "W":
            return "W"
        elif letter == "X":
            return "X"
        elif letter == "Y":
            return "Y"
        elif letter == "Z":
            return "Z"
        if letter == "a":
            return "A"
        elif letter == "b":
            return "B"
        elif letter == "c":
            return "C"
        elif letter == "d":
            return "D"
        elif letter == "e":
            return "E"
        elif letter == "f":
            return "F"
        elif letter == "g":
            return "G"
        elif letter == "h":
            return "H"
        elif letter == "i":
            return "I"
        elif letter == "j":
            return "J"
        elif letter == "k":
            return "K"
        elif letter == "l":
            return "L"
        elif letter == "m":
            return "M"
        elif letter == "n":
            return "N"
        elif letter == "o":
            return "O"
        elif letter == "p":
            return "P"
        elif letter == "q":
            return "Q"
        elif letter == "r":
            return "R"
        elif letter == "s":
            return "S"
        elif letter == "t":
            return "T"
        elif letter == "u":
            return "U"
        elif letter == "v":
            return "V"
        elif letter == "w":
            return "W"
        elif letter == "x":
            return "X"
        elif letter == "y":
            return "Y"
        elif letter == "z":
            return "Z"
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
        else:
            return "Error"

def capson(mystring):
    statement=""
    for letter in mystring:
        statement=statement+caps(letter)
    return statement

def nocaps(myletter):
    for letter in myletter:
        if letter == "A":
            return "a"
        elif letter == "B":
            return "b"
        elif letter == "C":
            return "c"
        elif letter == "D":
            return "d"
        elif letter == "E":
            return "e"
        elif letter == "F":
            return "f"
        elif letter == "G":
            return "g"
        elif letter == "H":
            return "h"
        elif letter == "I":
            return "i"
        elif letter == "J":
            return "j"
        elif letter == "K":
            return "k"
        elif letter == "L":
            return "l"
        elif letter == "M":
            return "m"
        elif letter == "N":
            return "n"
        elif letter == "O":
            return "o"
        elif letter == "P":
            return "p"
        elif letter == "Q":
            return "q"
        elif letter == "R":
            return "r"
        elif letter == "S":
            return "s"
        elif letter == "T":
            return "t"
        elif letter == "U":
            return "u"
        elif letter == "V":
            return "v"
        elif letter == "W":
            return "w"
        elif letter == "X":
            return "x"
        elif letter == "Y":
            return "y"
        elif letter == "Z":
            return "z"
        if letter == "a":
            return "a"
        elif letter == "b":
            return "b"
        elif letter == "c":
            return "c"
        elif letter == "d":
            return "d"
        elif letter == "e":
            return "e"
        elif letter == "f":
            return "f"
        elif letter == "g":
            return "g"
        elif letter == "h":
            return "h"
        elif letter == "i":
            return "i"
        elif letter == "j":
            return "j"
        elif letter == "k":
            return "k"
        elif letter == "l":
            return "l"
        elif letter == "m":
            return "m"
        elif letter == "n":
            return "n"
        elif letter == "o":
            return "o"
        elif letter == "p":
            return "p"
        elif letter == "q":
            return "q"
        elif letter == "r":
            return "r"
        elif letter == "s":
            return "s"
        elif letter == "t":
            return "t"
        elif letter == "u":
            return "u"
        elif letter == "v":
            return "v"
        elif letter == "w":
            return "w"
        elif letter == "x":
            return "x"
        elif letter == "y":
            return "y"
        elif letter == "z":
            return "z"
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
        else:
            return "Error"

def capsoff(mystring):
    statement=""
    for letter in mystring:
        statement=statement+nocaps(letter)
    return statement
