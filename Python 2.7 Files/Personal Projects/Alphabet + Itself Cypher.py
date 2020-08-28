def plusitselfencypher(mymessage):
    finalstring = ''
    for letter in mymessage:
        if letter == "Error":
            finalstring = "Error: Unrecognized input. Please try again."
            return finalstring
        else:
            finalstring = finalstring + plusitselfencypherkey(letter)
    return finalstring

def plusitselfdecypher(mymessage):
    finalstring = ''
    for letter in mymessage:
         if letter == "Error":
             finalstring = "Error: Unrecognized input. Please try again."
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
