def squareitselfencypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Unrecognized input. Please try again."
            return finalstring
        else:
            finalstring = finalstring + squareitselfencypherkey(letter)
    return finalstring

def squareitselfdecypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Unrecognized input. Please try again."
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
