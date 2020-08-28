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
    if letter == "a":
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

def caesarcypher(message):
    encoded = ""
    for letter in message:
        if CaesarCypherHelp(letter)=="Error":
            encoded = "Error: Incorrect character. Please try again."
            return encoded
        else:
            encoded=encoded+CaesarCypherHelp(letter)
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
    if letter == "a":
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

def ceasardecypher(message):
    decyphered = ""
    for letter in message:
        if CaesarDecypherHelp(letter)=="Error":
            decyphered = "Error: Incorrect character. Please try again."
            return decyphered
        else:
            decyphered = decyphered + CaesarDecypherHelp(letter)
    return decyphered
