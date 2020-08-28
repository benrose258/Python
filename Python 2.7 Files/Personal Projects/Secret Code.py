#Secret Code: Reverse Alphabet
def reversal(x):
    if x=="A":
        return "Z"
    elif x=="B":
        return "Y"
    elif x=="C":
        return "X"
    elif x=="D":
        return "W"
    elif x=="E":
        return "V"
    elif x=="F":
        return "U"
    elif x=="G":
        return "T"
    elif x=="H":
        return "S"
    elif x=="I":
        return "R"
    elif x=="J":
        return "Q"
    elif x=="K":
        return "P"
    elif x=="L":
        return "O"
    elif x=="M":
        return "N"
    elif x=="N":
        return "M"
    elif x=="O":
        return "L"
    elif x=="P":
        return "K"
    elif x=="Q":
        return "J"
    elif x=="R":
        return "I"
    elif x=="S":
        return "H"
    elif x=="T":
        return "G"
    elif x=="U":
        return "F"
    elif x=="V":
        return "E"
    elif x=="W":
        return "D"
    elif x=="X":
        return "C"
    elif x=="Y":
        return "B"
    elif x=="Z":
        return "A"
    elif x==" ":
        return " "
    else:
        return "Error: Incorrect input. Please try again."

def secretcode(decoded):
    if decoded=="":
        return "Error: No received input. Please try again."
    else:
        encoded=""
        for letter in decoded:
            encoded=encoded+reversal(letter)
        return encoded
