#Homework 6
#2

def double_strand(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        reverse=""
        for letter in string1:
            if letter == "A":
                reverse = reverse + "T"
            elif letter == "T":
                reverse = reverse + "A"
            elif letter == "G":
                reverse = reverse + "C"
            elif letter == "C":
                reverse = reverse + "G"
    if reverse != string2:
        return False
    else:
        return True
