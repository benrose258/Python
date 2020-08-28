def pokemonheal(pokemoncenter,mypokemon,currenthp,maxhp):
    if pokemoncenter==True:
        nursejoy = input("Welcome to the Pokemon Center! Would you like to heal your "+mypokemon+" to full health? ('Yes' or 'No')")
        if nursejoy == "Yes":
            return "Congratulations! Your "+mypokemon+" has been restored to full health!"
        else:
            return "You left your "+mypokemon+" to die in a hospital after refusing to give it treatment. You have to live with that forever, you murderer. Goodbye."
    else:
        if maxhp==currenthp:
            return "Your "+mypokemon+" is already at full health. There is no need to use an item."
        elif currenthp==0:
            print "Use a max revive, revival herb, or a revive to restore your "+mypokemon+"'s health."
        elif maxhp<=currenthp+20:
            print "Use a potion to restore your "+mypokemon+" to full health."
        elif maxhp<=currenthp+50:
            print "Use a super potion or an energy powder to restore your "+mypokemon+"to full health."
        elif maxhp<=currenthp+100:
            print "Use a Moo Moo Milk to restore your "+mypokemon+" to full health."
        elif maxhp<=currenthp+200:
            print "Use a hyper potion to restore your "+mypokemon+" to full health."
        elif maxhp>currenthp+200:
            print "Use a max potion or a full restore to restore your "+mypokemon+" to full health."

        willyouheal=input("Will you restore your "+mypokemon+" to full health? ('Yes' or 'No')")
        if willyouheal == "Yes":
            return "Your "+mypokemon+" has been restored to full health!"
        elif willyouheal == "No":
            return "Your "+mypokemon+" has fainted."
        else:
            return "Error: Incorrect input. Please try again."


'''This program will see if first you are at the pokemon center, if you are,
then it will heal and say "thanks, your pokemon have been restored to full health.
If not, it will check if the max hp minus the current hp is more than 20 (if it
is 20 or less, then say use potion), if it is more than 50(if it is between 21 and 50,
then say use super potion), if it is more than 200(if it is between 51 and 200,
then say use a hyper potion), or if it is more than 200(say use a full restore
or a max potion). If you aren't at the pokemon center, print "Also, you can go
to the pokemon center to heal your pokemon." At the current time, this will take
1 pokemon in and output your required healing. Also, if your pokemon are fully
healed(your max hp minus your current hp equals 0), then say "Your pokemon are
fully healed. Do not use healing items." If the currenthp is equivalent to 0,
then say "Use a revive or a max revive."'''

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
