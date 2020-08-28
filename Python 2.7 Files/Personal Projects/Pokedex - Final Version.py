D = {}

def pokedex():
    pokemonlist = ["Bulbasaur","Ivysaur","Venasaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran(F)","Nidorina","Nidoqueen","Nidoran(M)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetails","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew","Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Quilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-Oh","Celebi","Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys","Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Primplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Wormadam","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime Jr.","Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Probopass","Dusknoir","Froslass","Rotom","Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina",
"Cresselia","Phione","Manaphy","Darkrai","Shaymin","Arceus","Victini","Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Valillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus","Thundurus","Reshiram","Zekrom","Landorus","Kyurem","Keldeo","Meloetta","Genesect","Chespin","Quilladin","Chesnaught","Fennekin","Braixen","Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa","Vivillon","Litleo","Pyroar","Flab"b"","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic","Honedge","Doublade","Aegislash","Spritzee","Aromatisse","Swirlix","Slurpuff","Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt","Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant","Pumpkaboo","Gourgeist","Bergmite","Avalugg","Noibat","Noivern","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Volcanion"]
    typelist = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"]
    print "Dexter Version 3.0.5"
    print ""
    print "Clear Page: (0)"
    print "Search Pokemon by number: (1)"
    print "Search all Pokemon an interval: (2)"
    print "Search by reigonal pokedex: (3)"
    print "Search Pokemon by name: (4)"
    print "Pokemon Type Effectiveness: (5)"
    print ""
    whatfeature = input("Which of the above features would you like to use? ")
    if whatfeature == 1:
        searchbynumber(pokemonlist)
    elif whatfeature == 2:
        searchbyinterval(pokemonlist)
    elif whatfeature == 3:
        searchbyregion(pokemonlist)
    elif whatfeature == 4:
        pokemonnames()
    elif whatfeature == 5:
        typecharts(typelist)
    elif whatfeature == 0:
        for index in range(0,50):
            print ""
        return pokedex()
    wannacontinue = input("Would you like to keep using Dexter? ")
    print ""
    if wannacontinue == True or wannacontinue == Yes or wannacontinue == yes:
        return pokedex()
    else:
        print "Thank you for using Dexter. Goodbye."
        exit

def searchbynumber(pokemonlist):
    print ""
    whichpokemon = input("Which pokemon are you looking for? (By number) ")
    print "Pokedex Entry",whichpokemon,": "+str(pokemonlist[whichpokemon-1])
    searchagain = input("Would you like to search for another pokemon? ")
    if searchagain == Yes or searchagain == yes or searchagain == True:
        return searchbynumber(pokemonlist)
    else:
        exit

def blahtest(x,y):
    numberlist = range(x,y+1)
    for index in numberlist:
        print index
def intervalEntryNumbers(firstnumber,lastnumber,index):
    numberlist = range(firstnumber,lastnumber+1)
    return numberlist[index]

#def recursiveintervaldisplay(firstnumber,lastnumber):

#Search youtube for python tkinter to make a GUI for the program

def searchbyinterval(pokemonlist):
    print ""
    print "What interval would you like to display?"
    firstnumber = input("First number: ")
    lastnumber = input("Last number: ")
    mylist = pokemonlist[firstnumber-1:lastnumber]
    print "Here are the pokemon from "+str(firstnumber)+" to "+str(lastnumber)+":"
    pokemoninterval = intervalnumberdisplay(firstnumber,mylist)
    counter = 0
    for index in range(len(pokemoninterval)):
        print "Pokemon Number "+str(counter+firstnumber)+": "+pokemoninterval[index]
        counter = counter + 1
    print ""
    anotherinterval = input("Would you like to search another interval? ")
    if anotherinterval == True or anotherinterval == Yes or anotherinterval==yes:
        return searchbyinterval(pokemonlist)
    else:
        print ""
        exit

def intervalnumberdisplay(currentnumber,mylist):
    if mylist == []:
        return []
    else:
        return [mylist[0]] + intervalnumberdisplay(currentnumber+1,mylist[1:])

def searchbyregion(pokemonlist):
    print ""
    whichregion = input("Which region's pokedex would you like to view? ('Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos')")
    if whichregion == "Kanto":
        currentpokemon = 1
        kantolist = pokemonlist[0:151]
        if (tuple(kantolist)) in D:
            for index in D[(tuple(kantolist))]:
                print "Kanto Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
        else:
            D[(tuple(kantolist))] = tuple(kantolist)
            for index in kantolist:
                print "Kanto Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
    elif whichregion == "Johto":
        currentpokemon = 1
        johtolist = pokemonlist[151:251]
        if (tuple(johtolist)) in D:
            for index in D[(tuple(johtolist))]:
                print "Johto Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
        else:
            D[(tuple(johtolist))] = tuple(johtolist)
            for index in johtolist:
                print "Johto Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
    elif whichregion == "Hoenn":
        currentpokemon = 1
        hoennlist = pokemonlist[251:386]
        if (tuple(hoennlist)) in D:
            for index in D[(tuple(hoennlist))]:
                print "Hoenn Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon=currentpokemon+1
        else:
            D[(tuple(hoennlist))] = tuple(hoennlist)
            for index in hoennlist:
                print "Hoenn Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon=currentpokemon+1
    elif whichregion == "Sinnoh":
        currentpokemon = 1
        sinnohlist = pokemonlist[386:493]
        if (tuple(sinnohlist)) in D:
            for index in D[(tuple(sinnohlist))]:
                print "Sinnoh Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
        else:
            D[(tuple(sinnohlist))] = tuple(sinnohlist)
            for index in sinnohlist:
                print "Sinnoh Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
    elif whichregion == "Unova":
        currentpokemon = 0
        unovalist = pokemonlist[493:649]
        if (tuple(unovalist)) in D:
            for index in D[(tuple(unovalist))]:
                print "Unova Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon + 1
        else:
            D[(tuple(unovalist))] = tuple(unovalist)
            for index in unovalist:
                print "Unova Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon + 1
    elif whichregion == "Kalos":
        currentpokemon = 1
        kaloslist = pokemonlist[649:]
        if (tuple(kaloslist)) in D:
            for index in D[(tuple(kaloslist))]:
                print "Kalos Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon + 1
        else:
            for index in kaloslist:
                print "Kalos Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon + 1
    else:
        print "You have input an incorrect reigon. Please restart the program and try again."
    print ""
    anotherregion = input("Would you like to search another region? ")
    if anotherregion == True or anotherregion == Yes or anotherregion==yes:
        return searchbyregion(pokemonlist)
    else:
        exit

def Yes():
    return "Yes"

def yes():
    return "Yes"

def No():
    return "No"

def no():
    return "No"

def typecharts(typelist):
    print ""
    print "List pokemon types: (1)"
    print "List pokemon type effectiveness: (2)"
    print ""
    typefunctions = input("Which of the above type functions would you like to use? ")
    if typefunctions == 1:
        typenumber = 0
        for eachtype in typelist:
            print "Type "+str(typenumber)+": "+str(eachtype)
            typenumber = typenumber + 1
    if typefunctions == 2:
        def printitems(MyEffectiveTypesList,AttackOrDefense,mytype,howeffective,SuperNoNotRegular):
            if AttackOrDefense == "Attack":
                AttackOrDefense = "Attack"
            elif AttackOrDefense == "Defense":
                AttackOrDefense = "Defense"

            if howeffective == 2:
                return "2x"
            elif howeffective == 0.5:
                howeffective = "1/2x"
            elif howeffective == 0:
                howeffective = "0x"
            elif howeffective == 1:
                howeffective = "1x"

            if SuperNoNotRegular == "Super":
                SuperNoNotRegular = "Super-effective"
            elif SuperNoNotRegular == "No":
                SuperNoNotRegular = "Not effective"
            elif SuperNoNotRegular == "Not":
                SuperNoNotRegular = "Not very effective"
            elif SuperNoNotRegular == "Regular":
                SuperNoNotRegular = "Regularly effective"

            if MyEffectiveTypesList == []:
                MyEffectiveTypesList = ["None"]

            print str(mytype)+" Type "+str(AttackOrDefense)+" Effectiveness:"
            print ""
            print str(SuperNoNotRegular)+"("+str(howeffective)+"x)"+":"
            print ""
            for index in MyEffectiveTypesList:
                print index
            print ""

        typenumber = 1
        for eachtype in typelist:
            print str(eachtype)+": "+"("+str(typenumber)+")"
            typenumber = typenumber + 1
        choosetype = input("Which of the above types would you like to view? ")
        print ""
        if choosetype == 1:
            print "Normal Type Attack Effectiveness:"
            print ""
            print "Super-effective(2x):"
            print "None"
            print ""
            print "Not very effective(1/2x):"
            print typelist[12]
            print typelist[17]
            print ""
            print "No effect(0x):"
            print typelist[13]
            print ""
            print "Regular effectiveness(1x):"
            for index in range(0,11):
                print typelist[index]
            print typelist[14]
            print typelist[15]
            print typelist[17]
            print ""
            print "Normal Type Defense Effectiveness:"
            print ""
            print 'Super-effective(2x):'
            print typelist[6]
            print ""
            print "Not very effective(1/2x):"
            print "None"
            print ""
            print "No effect(0x):"
            print typelist[13]
            print ""
            print "Regular effectiveness(1x):"
            for index in range(0,5):
                print typelist[index]
            for index in range(7,12):
                print typelist[index]
            for index in range(14,17):
                print typelist[index]

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","","1","Regular")

        elif choosetype == 2:
            printitems([str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[11]),str(typelist[16])],"Attack","Fire","2","Super")
            printitems([str(typelist[1]),str(typelist[2]),str(typelist[12]),str(typelist[14])],"Attack","Fire","1/2","Not")
            printitems([],"Attack","Fire","0","No")
            printitems([str(typelist[0]),str(typelist[3]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[13]),str(typelist[15]),str(typelist[17])],"Attack","Fire","1","Regular")

            printitems([str(typelist[2]),str(typelist[8]),str(typelist[12])],"Defense","Fire","2","Super")
            printitems([str(typelist[1]),str(typelist[4]),str(typelist[5]),str(typelist[11]),str(typelist[16]),str(typelist[17])],"Defense","Fire","1/2","Not")
            printitems([],"Defense","Fire","0","No")
            printitems([str(typelist[0]),str(typelist[3]),str(typelist[6]),str(typelist[7]),str(typelist[9]),str(typelist[10]),str(typelist[13]),str(typelist[14]),str(typelist[15])],"Defense","Fire","1","Regular")

        elif choosetype == 3:
            printitems([str(typelist[1]),str(typelist[8]),str(typelist[12])],"Attack","Water","2","Super")
            printitems([str(typelist[2]),str(typelist[4]),str(typelist[14])],"Attack","Water","1/2","Not")
            printitems([],"Attack","Water","0","No")
            printitems([str(typelist[0]),str(typelist[3]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[13]),str(typelist[15]),str(typelist[17])],"Attack","Water","1","Regular")

            printitems([str(typelist[3]),str(typelist[4])],"Defense","Water","2","Super")
            printitems([str(typelist[1]),str(typelist[2]),str(typelist[5]),str(typelist[16])],"Defense","Water","1/2","Not")
            printitems([],"Defense","Water","0","No")
            printitems([str(typelist[0]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[17])],"Defense","Water","1","Regular")

        elif choosetype == 4:
            printitems([str(typelist[2]),str(typelist[9])],"Attack","Electric","2","Super")
            printitems([str(typelist[3]),str(typelist[4]),str(typelist[14])],"Attack","Electric","1/2","Not")
            printitems([str(typelist[8])],"Attack","Electric","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[13]),str(typelist[15]),str(typelist[17])],"Attack","Electric","1","Regular")

            printitems([str(typelist[8])],"Defense","Electric","2","Super")
            printitems([str(typelist[3]),str(typelist[9]),str(typelist[16])],"Defense","Electric","1/2","Not")
            printitems([],"Defense","Electric","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[17])],"Defense","Electric","1","Regular")

        elif choosetype == 5:
            printitems([str(typelist[2]),str(typelist[8]),str(typelist[12])],"Attack","Grass","2","Super")
            printitems([str(typelist[1]),str(typelist[4]),str(typelist[7]),str(typelist[9]),str(typelist[11]),str(typelist[14])],"Attack","Grass","1/2","Not")
            printitems([],"Attack","Grass","0","No")
            printitems([str(typelist[0]),str(typelist[3]),str(typelist[5]),str(typelist[6]),str(typelist[10]),str(typelist[13]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Grass","1","Regular")

            printitems([str(typelist[1]),str(typelist[5]),str(typelist[7]),str(typelist[9]),str(typelist[11])],"Defense","Grass","2","Super")
            printitems([str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[8])],"Defense","Grass","1/2","Not")
            printitems([],"Defense","Grass","0","No")
            printitems([str(typelist[0]),str(typelist[6]),str(typelist[10]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Grass","1","Regular")

        elif choosetype == 6:
            printitems([str(typelist[4]),str(typelist[8]),str(typelist[9]),str(typelist[14])],"Attack","Ice","2","Super")
            printitems([str(typelist[1]),str(typelist[2]),str(typelist[5]),str(typelist[16])],"Attack","Ice","1/2","Not")
            printitems([],"Attack","Ice","0","No")
            printitems([str(typelist[0]),str(typelist[3]),str(typelist[6]),str(typelist[7]),str(typelist[10]),str(typelist[11]),str(typelist[13]),str(typelist[15]),str(typelist[17])],"Attack","Ice","1","Regular")

            printitems([str(typelist[1]),str(typelist[6]),str(typelist[12]),str(typelist[16])],"Defense","Ice","2","Super")
            printitems([str(typelist[5])],"Defense","Ice","1/2","Not")
            printitems([],"Defense","Ice","0","No")
            printitems([str(typelist[0]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[17])],"Defense","Ice","1","Regular")

        elif choosetype == 7:
            printitems([str(typelist[0]),str(typelist[5]),str(typelist[12]),str(typelist[15]),str(typelist[16])],"Attack","Fighting","2","Super")
            printitems([str(typelist[7]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[17])],"Attack","Fighting","1/2","Not")
            printitems([str(typelist[13])],"Attack","Fighting","0","No")
            printitems([str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[6]),str(typelist[8]),str(typelist[14])],"Attack","Fighting","1","Regular")

            printitems([str(typelist[9]),str(typelist[10]),str(typelist[17])],"Defense","Fighting","2","Super")
            printitems([str(typelist[11]),str(typelist[12]),str(typelist[15])],"Defense","Fighting","1/2","Not")
            printitems([],"Defense","Fighting","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[13]),str(typelist[14]),str(typelist[16])],"Defense","Fighting","1","Regular")

        elif choosetype == 8:
            printitems([str(typelist[4]),str(typelist[17])],"Attack","Poison","2","Super")
            printitems([str(typelist[7]),str(typelist[8]),str(typelist[12]),str(typelist[13])],"Attack","Poison","1/2","Not")
            printitems([str(typelist[16])],"Attack","Poison","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[5]),str(typelist[6]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[14]),str(typelist[15])],"Attack","Poison","1","Regular")

            printitems([str(typelist[8]),str(typelist[10])],"Defense","Poison","2","Super")
            printitems([str(typelist[4]),str(typelist[6]),str(typelist[7]),str(typelist[11]),str(typelist[17])],"Defense","Poison","1/2","Not")
            printitems([],"Defense","Poison","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[5]),str(typelist[9]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16])],"Defense","Poison","1","Regular")

        elif choosetype == 9:
            printitems([str(typelist[1]),str(typelist[3]),str(typelist[7]),str(typelist[12]),str(typelist[16])],"Attack","Ground","2","Super")
            printitems([str(typelist[4]),str(typelist[11])],"Attack","Ground","1/2","Not")
            printitems([str(typelist[9])],"Attack","Ground","0","No")
            printitems([str(typelist[0]),str(typelist[2]),str(typelist[5]),str(typelist[6]),str(typelist[8]),str(typelist[10]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[17])],"Attack","Ground","1","Regular")

            printitems([str(typelist[2]),str(typelist[4]),str(typelist[5])],"Defense","Ground","2","Super")
            printitems([str(typelist[7]),str(typelist[12])],"Defense","Ground","1/2","Not")
            printitems([str(typelist[3])],"Defense","Ground","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[6]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Ground","1","Regular")

        #FLYING ONWARD ISN'T DONE, SO DO FLYING ONWARD. AGAIN, GOOD JOB, I KNOW THIS IS A PAIN.
        elif choosetype == 10: #"Flying"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Flying","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Flying","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Flying","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Flying","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Flying","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Flying","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Flying","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Flying","1","Regular")

        elif choosetype == 11: #"Psychic"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Psychic","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Psychic","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Psychic","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Psychic","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Psychic","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Psychic","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Psychic","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Psychic","1","Regular")

        elif choosetype == 12: #"Bug"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Bug","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Bug","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Bug","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Bug","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Bug","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Bug","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Bug","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Bug","1","Regular")

        elif choosetype == 13: #"Rock"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Rock","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Rock","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Rock","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Rock","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Rock","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Rock","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Rock","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Rock","1","Regular")

        elif choosetype == 14: #"Ghost"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Ghost","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Ghost","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Ghost","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Ghost","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Ghost","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Ghost","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Ghost","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Ghost","1","Regular")

        elif choosetype == 15: #"Dragon"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dragon","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dragon","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dragon","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dragon","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dragon","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dragon","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dragon","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dragon","1","Regular")

        elif choosetype == 16: #"Dark"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dark","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dark","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dark","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Dark","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dark","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dark","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dark","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Dark","1","Regular")

        elif choosetype == 17: #"Steel"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Steel","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Steel","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Steel","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Steel","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Steel","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Steel","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Steel","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Steel","1","Regular")

        elif choosetype == 18: #"Fairy"
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Fairy","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Fairy","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Fairy","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Attack","Fairy","1","Regular")

            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Fairy","2","Super")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Fairy","1/2","Not")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Fairy","0","No")
            printitems([str(typelist[0]),str(typelist[1]),str(typelist[2]),str(typelist[3]),str(typelist[4]),str(typelist[5]),str(typelist[6]),str(typelist[7]),str(typelist[8]),str(typelist[9]),str(typelist[10]),str(typelist[11]),str(typelist[12]),str(typelist[13]),str(typelist[14]),str(typelist[15]),str(typelist[16]),str(typelist[17])],"Defense","Fairy","1","Regular")

    print ""
    keepgoing = input("Would you like to use another pokemon typing function? ")
    if keepgoing == True or keepgoing == Yes or keepgoing==yes:
        return typecharts(typelist)
    else:
        exit


def pokemonnames():
    print ""
    pokemon = input("Please type the name of the Pokemon you would like to search... ")
    print ""
    if pokemon == "Bulbasaur":
        print 'Pokedex Entry '+str(1)+""
    elif pokemon == "Ivysaur":
        print 'Pokedex Entry '+str(2)+""
    elif pokemon == "Venasaur":
        print 'Pokedex Entry '+str(3)+""
    elif pokemon == "Charmander":
        print 'Pokedex Entry '+str(4)+""
    elif pokemon == "Charmeleon":
        print 'Pokedex Entry '+str(5)+""
    elif pokemon == "Charizard":
        print 'Pokedex Entry '+str(6)+""
    elif pokemon == "Squirtle":
        print 'Pokedex Entry '+str(7)+""
    elif pokemon == "Wartortle":
        print 'Pokedex Entry '+str(8)+""
    elif pokemon == "Blastoise":
        print 'Pokedex Entry '+str(9)+""
    elif pokemon == "Caterpie":
        print 'Pokedex Entry '+str(10)+""
    elif pokemon == "Metapod":
        print 'Pokedex Entry '+str(11)+""
    elif pokemon == "Butterfree":
        print 'Pokedex Entry '+str(12)+""
    elif pokemon == "Weedle":
        print 'Pokedex Entry '+str(13)+""
    elif pokemon == "Kakuna":
        print 'Pokedex Entry '+str(14)+""
    elif pokemon == "Beedrill":
        print 'Pokedex Entry '+str(15)+""
    elif pokemon == "Pidgey":
        print 'Pokedex Entry '+str(16)+""
    elif pokemon == "Pidgeotto":
        print 'Pokedex Entry '+str(17)+""
    elif pokemon == "Pidgeot":
        print 'Pokedex Entry '+str(18)+""
    elif pokemon == "Rattata":
        print 'Pokedex Entry '+str(19)+""
    elif pokemon == "Raticate":
        print 'Pokedex Entry '+str(20)+""
    elif pokemon == "Spearow":
        print 'Pokedex Entry '+str(21)+""
    elif pokemon == "Fearow":
        print 'Pokedex Entry '+str(22)+""
    elif pokemon == "Ekans":
        print 'Pokedex Entry '+str(23)+""
    elif pokemon == "Arbok":
        print 'Pokedex Entry '+str(24)+""
    elif pokemon == "Pikachu":
        print 'Pokedex Entry '+str(25)+""
    elif pokemon == "Raichu":
        print 'Pokedex Entry '+str(26)+""
    elif pokemon == "Sandshrew":
        print 'Pokedex Entry '+str(27)+""
    elif pokemon == "Sandslash":
        print 'Pokedex Entry '+str(28)+""
    elif pokemon == "Nidoran(F)":
        print 'Pokedex Entry '+str(29)+""
    elif pokemon == "Nidorina":
        print 'Pokedex Entry '+str(30)+""
    elif pokemon == "Nidoqueen":
        print 'Pokedex Entry '+str(31)+""
    elif pokemon == "Nidoran(M)":
        print 'Pokedex Entry '+str(32)+""
    elif pokemon == "Nidorino":
        print 'Pokedex Entry '+str(33)+""
    elif pokemon == "Nidoking":
        print 'Pokedex Entry '+str(34)+""
    elif pokemon == "Clefairy":
        print 'Pokedex Entry '+str(35)+""
    elif pokemon == "Clefable":
        print 'Pokedex Entry '+str(36)+""
    elif pokemon == "Vulpix":
        print 'Pokedex Entry '+str(37)+""
    elif pokemon == "Ninetails":
        print 'Pokedex Entry '+str(38)+""
    elif pokemon == "Jigglypuff":
        print 'Pokedex Entry '+str(39)+""
    elif pokemon == "Wigglytuff":
        print 'Pokedex Entry '+str(40)+""
    elif pokemon == "Zubat":
        print 'Pokedex Entry '+str(41)+""
    elif pokemon == "Golbat":
        print 'Pokedex Entry '+str(42)+""
    elif pokemon == "Oddish":
        print 'Pokedex Entry '+str(43)+""
    elif pokemon == "Gloom":
        print 'Pokedex Entry '+str(44)+""
    elif pokemon == "Vileplume":
        print 'Pokedex Entry '+str(45)+""
    elif pokemon == "Paras":
        print 'Pokedex Entry '+str(46)+""
    elif pokemon == "Parasect":
        print 'Pokedex Entry '+str(47)+""
    elif pokemon == "Venonat":
        print 'Pokedex Entry '+str(48)+""
    elif pokemon == "Venomoth":
        print 'Pokedex Entry '+str(49)+""
    elif pokemon == "Diglett":
        print 'Pokedex Entry '+str(50)+""
    elif pokemon == "Dugtrio":
        print 'Pokedex Entry '+str(51)+""
    elif pokemon == "Meowth":
        print 'Pokedex Entry '+str(52)+""
    elif pokemon == "Persian":
        print 'Pokedex Entry '+str(53)+""
    elif pokemon == "Psyduck":
        print 'Pokedex Entry '+str(54)+""
    elif pokemon == "Golduck":
        print 'Pokedex Entry '+str(55)+""
    elif pokemon == "Mankey":
        print 'Pokedex Entry '+str(56)+""
    elif pokemon == "Primape":
        print 'Pokedex Entry '+str(57)+""
    elif pokemon == "Growlithe":
        print 'Pokedex Entry '+str(58)+""
    elif pokemon == "Arcanine":
        print 'Pokedex Entry '+str(59)+""
    elif pokemon == "Poliwag":
        print 'Pokedex Entry '+str(60)+""
    elif pokemon == "Poliwhirl":
        print 'Pokedex Entry '+str(61)+""
    elif pokemon == "Poliwrath":
        print 'Pokedex Entry '+str(62)+""
    elif pokemon == "Abra":
        print 'Pokedex Entry '+str(63)+""
    elif pokemon == "Kadabra":
        print 'Pokedex Entry '+str(64)+""
    elif pokemon == "Alakazam":
        print 'Pokedex Entry '+str(65)+""
    elif pokemon == "Machop":
        print 'Pokedex Entry '+str(66)+""
    elif pokemon == "Machoke":
        print 'Pokedex Entry '+str(67)+""
    elif pokemon == "Machamp":
        print 'Pokedex Entry '+str(68)+""
    elif pokemon == "Bellsprout":
        print 'Pokedex Entry '+str(69)+""
    elif pokemon == "Weepinbell":
        print 'Pokedex Entry '+str(70)+""
    elif pokemon == "Victreebel":
        print 'Pokedex Entry '+str(71)+""
    elif pokemon == "Tentacool":
        print 'Pokedex Entry '+str(72)+""
    elif pokemon == "Tentacruel":
        print 'Pokedex Entry '+str(73)+""
    elif pokemon == "Geodude":
        print 'Pokedex Entry '+str(74)+""
    elif pokemon == "Graveler":
        print 'Pokedex Entry '+str(75)+""
    elif pokemon == "Golem":
        print 'Pokedex Entry '+str(76)+""
    elif pokemon == "Ponyta":
        print 'Pokedex Entry '+str(77)+""
    elif pokemon == "Rapidash":
        print 'Pokedex Entry '+str(78)+""
    elif pokemon == "Slowpoke":
        print 'Pokedex Entry '+str(79)+""
    elif pokemon == "Slowbro":
        print 'Pokedex Entry '+str(80)+""
    elif pokemon == "Magnemite":
        print 'Pokedex Entry '+str(81)+""
    elif pokemon == "Magneton":
        print 'Pokedex Entry '+str(82)+""
    elif pokemon == "Farfetch'd":
        print 'Pokedex Entry '+str(83)+""
    elif pokemon == "Doduo":
        print 'Pokedex Entry '+str(84)+""
    elif pokemon == "Dodrio":
        print 'Pokedex Entry '+str(85)+""
    elif pokemon == "Seel":
        print 'Pokedex Entry '+str(86)+""
    elif pokemon == "Dewgong":
        print 'Pokedex Entry '+str(87)+""
    elif pokemon == "Grimer":
        print 'Pokedex Entry '+str(88)+""
    elif pokemon == "Muk":
        print 'Pokedex Entry '+str(89)+""
    elif pokemon == "Shellder":
        print 'Pokedex Entry '+str(90)+""
    elif pokemon == "Cloyster":
        print 'Pokedex Entry '+str(91)+""
    elif pokemon == "Gastly":
        print 'Pokedex Entry '+str(92)+""
    elif pokemon == "Haunter":
        print 'Pokedex Entry '+str(93)+""
    elif pokemon == "Gengar":
        print 'Pokedex Entry '+str(94)+""
    elif pokemon == "Onix":
        print 'Pokedex Entry '+str(95)+""
    elif pokemon == "Drowzee":
        print 'Pokedex Entry '+str(96)+""
    elif pokemon == "Hypno":
        print 'Pokedex Entry '+str(97)+""
    elif pokemon == "Krabby":
        print 'Pokedex Entry '+str(98)+""
    elif pokemon == "Kingler":
        print 'Pokedex Entry '+str(99)+""
    elif pokemon == "Voltorb":
        print 'Pokedex Entry '+str(100)+""
    elif pokemon == "Electrode":
        print 'Pokedex Entry '+str(101)+""
    elif pokemon == "Exeggcute":
        print 'Pokedex Entry '+str(102)+""
    elif pokemon == "Exeggutor":
        print 'Pokedex Entry '+str(103)+""
    elif pokemon == "Cubone":
        print 'Pokedex Entry '+str(104)+""
    elif pokemon == "Marowak":
        print 'Pokedex Entry '+str(105)+""
    elif pokemon == "Hitmonlee":
        print 'Pokedex Entry '+str(106)+""
    elif pokemon == "Hitmonchan":
        print 'Pokedex Entry '+str(107)+""
    elif pokemon == "Lickitung":
        print 'Pokedex Entry '+str(108)+""
    elif pokemon == "Koffing":
        print 'Pokedex Entry '+str(109)+""
    elif pokemon == "Weezing":
        print 'Pokedex Entry '+str(110)+""
    elif pokemon == "Rhyhorn":
        print 'Pokedex Entry '+str(111)+""
    elif pokemon == "Rhydon":
        print 'Pokedex Entry '+str(112)+""
    elif pokemon == "Chansey":
        print 'Pokedex Entry '+str(113)+""
    elif pokemon == "Tangela":
        print 'Pokedex Entry '+str(114)+""
    elif pokemon == "Kangaskhan":
        print 'Pokedex Entry '+str(115)+""
    elif pokemon == "Horsea":
        print 'Pokedex Entry '+str(116)+""
    elif pokemon == "Seadra":
        print 'Pokedex Entry '+str(117)+""
    elif pokemon == "Goldeen":
        print 'Pokedex Entry '+str(118)+""
    elif pokemon == "Seaking":
        print 'Pokedex Entry '+str(119)+""
    elif pokemon == "Staryu":
        print 'Pokedex Entry '+str(120)+""
    elif pokemon == "Starmie":
        print 'Pokedex Entry '+str(121)+""
    elif pokemon == "Mr. Mime":
        print 'Pokedex Entry '+str(122)+""
    elif pokemon == "Scyther":
        print 'Pokedex Entry '+str(123)+""
    elif pokemon == "Jynx":
        print 'Pokedex Entry '+str(124)+""
    elif pokemon == "Electabuzz":
        print 'Pokedex Entry '+str(125)+""
    elif pokemon == "Magmar":
        print 'Pokedex Entry '+str(126)+""
    elif pokemon == "Pinsir":
        print 'Pokedex Entry '+str(127)+""
    elif pokemon == "Tauros":
        print 'Pokedex Entry '+str(128)+""
    elif pokemon == "Magikarp":
        print 'Pokedex Entry '+str(129)+""
    elif pokemon == "Gyarados":
        print 'Pokedex Entry '+str(130)+""
    elif pokemon == "Lapras":
        print 'Pokedex Entry '+str(131)+""
    elif pokemon == "Ditto":
        print 'Pokedex Entry '+str(132)+""
    elif pokemon == "Eevee":
        print 'Pokedex Entry '+str(133)+""
    elif pokemon == "Vaporeon":
        print 'Pokedex Entry '+str(134)+""
    elif pokemon == "Jolteon":
        print 'Pokedex Entry '+str(135)+""
    elif pokemon == "Flareon":
        print 'Pokedex Entry '+str(136)+""
    elif pokemon == "Porygon":
        print 'Pokedex Entry '+str(137)+""
    elif pokemon == "Omanyte":
        print 'Pokedex Entry '+str(138)+""
    elif pokemon == "Omastar":
        print 'Pokedex Entry '+str(139)+""
    elif pokemon == "Kabuto":
        print 'Pokedex Entry '+str(140)+""
    elif pokemon == "Kabutops":
        print 'Pokedex Entry '+str(141)+""
    elif pokemon == "Aerodactyl":
        print 'Pokedex Entry '+str(142)+""
    elif pokemon == "Snorlax":
        print 'Pokedex Entry '+str(143)+""
    elif pokemon == "Articuno":
        print 'Pokedex Entry '+str(144)+""
    elif pokemon == "Zapdos":
        print 'Pokedex Entry '+str(145)+""
    elif pokemon == "Moltres":
        print 'Pokedex Entry '+str(146)+""
    elif pokemon == "Dratini":
        print 'Pokedex Entry '+str(147)+""
    elif pokemon == "Dragonair":
        print 'Pokedex Entry '+str(148)+""
    elif pokemon == "Dragonite":
        print 'Pokedex Entry '+str(149)+""
    elif pokemon == "Mewtwo":
        print 'Pokedex Entry '+str(150)+""
    elif pokemon == "Mew":
        print 'Pokedex Entry '+str(151)+""
    elif pokemon == "Chikorita":
        print 'Pokedex Entry '+str(152)+""
    elif pokemon == "Bayleef":
        print 'Pokedex Entry '+str(153)+""
    elif pokemon == "Meganium":
        print 'Pokedex Entry '+str(154)+""
    elif pokemon == "Cyndaquil":
        print 'Pokedex Entry '+str(155)+""
    elif pokemon == "Quilava":
        print 'Pokedex Entry '+str(156)+""
    elif pokemon == "Typhlosion":
        print 'Pokedex Entry '+str(157)+""
    elif pokemon == "Totodile":
        print 'Pokedex Entry '+str(158)+""
    elif pokemon == "Croconaw":
        print 'Pokedex Entry '+str(159)+""
    elif pokemon == "Feraligatr":
        print 'Pokedex Entry '+str(160)+""
    elif pokemon == "Sentret":
        print 'Pokedex Entry '+str(161)+""
    elif pokemon == "Furret":
        print 'Pokedex Entry '+str(162)+""
    elif pokemon == "Hoothoot":
        print 'Pokedex Entry '+str(163)+""
    elif pokemon == "Noctowl":
        print 'Pokedex Entry '+str(164)+""
    elif pokemon == "Ledyba":
        print 'Pokedex Entry '+str(165)+""
    elif pokemon == "Ledian":
        print 'Pokedex Entry '+str(166)+""
    elif pokemon == "Spinarak":
        print 'Pokedex Entry '+str(167)+""
    elif pokemon == "Ariados":
        print 'Pokedex Entry '+str(168)+""
    elif pokemon == "Crobat":
        print 'Pokedex Entry '+str(169)+""
    elif pokemon == "Chinchou":
        print 'Pokedex Entry '+str(170)+""
    elif pokemon == "Lanturn":
        print 'Pokedex Entry '+str(171)+""
    elif pokemon == "Pichu":
        print 'Pokedex Entry '+str(172)+""
    elif pokemon == "Cleffa":
        print 'Pokedex Entry '+str(173)+""
    elif pokemon == "Igglybuff":
        print 'Pokedex Entry '+str(174)+""
    elif pokemon == "Togepi":
        print 'Pokedex Entry '+str(175)+""
    elif pokemon == "Togetic":
        print 'Pokedex Entry '+str(176)+""
    elif pokemon == "Natu":
        print 'Pokedex Entry '+str(177)+""
    elif pokemon == "Xatu":
        print 'Pokedex Entry '+str(178)+""
    elif pokemon == "Mareep":
        print 'Pokedex Entry '+str(179)+""
    elif pokemon == "Flaaffy":
        print 'Pokedex Entry '+str(180)+""
    elif pokemon == "Ampharos":
        print 'Pokedex Entry '+str(181)+""
    elif pokemon == "Bellossom":
        print 'Pokedex Entry '+str(182)+""
    elif pokemon == "Marill":
        print 'Pokedex Entry '+str(183)+""
    elif pokemon == "Azumarill":
        print 'Pokedex Entry '+str(184)+""
    elif pokemon == "Sudowoodo":
        print 'Pokedex Entry '+str(185)+""
    elif pokemon == "Politoed":
        print 'Pokedex Entry '+str(186)+""
    elif pokemon == "Hoppip":
        print 'Pokedex Entry '+str(187)+""
    elif pokemon == "Skiploom":
        print 'Pokedex Entry '+str(188)+""
    elif pokemon == "Jumpluff":
        print 'Pokedex Entry '+str(189)+""
    elif pokemon == "Aipom":
        print 'Pokedex Entry '+str(190)+""
    elif pokemon == "Sunkern":
        print 'Pokedex Entry '+str(191)+""
    elif pokemon == "Sunflora":
        print 'Pokedex Entry '+str(192)+""
    elif pokemon == "Yanma":
        print 'Pokedex Entry '+str(193)+""
    elif pokemon == "Wooper":
        print 'Pokedex Entry '+str(194)+""
    elif pokemon == "Quagsire":
        print 'Pokedex Entry '+str(195)+""
    elif pokemon == "Espeon":
        print 'Pokedex Entry '+str(196)+""
    elif pokemon == "Umbreon":
        print 'Pokedex Entry '+str(197)+""
    elif pokemon == "Murkrow":
        print 'Pokedex Entry '+str(198)+""
    elif pokemon == "Slowking":
        print 'Pokedex Entry '+str(199)+""
    elif pokemon == "Misdreavus":
        print 'Pokedex Entry '+str(200)+""
    elif pokemon == "Unown":
        print 'Pokedex Entry '+str(201)+""
    elif pokemon == "Wobbuffet":
        print 'Pokedex Entry '+str(202)+""
    elif pokemon == "Girafarig":
        print 'Pokedex Entry '+str(203)+""
    elif pokemon == "Pineco":
        print 'Pokedex Entry '+str(204)+""
    elif pokemon == "Forretress":
        print 'Pokedex Entry '+str(205)+""
    elif pokemon == "Dunsparce":
        print 'Pokedex Entry '+str(206)+""
    elif pokemon == "Gligar":
        print 'Pokedex Entry '+str(207)+""
    elif pokemon == "Steelix":
        print 'Pokedex Entry '+str(208)+""
    elif pokemon == "Snubbull":
        print 'Pokedex Entry '+str(209)+""
    elif pokemon == "Granbull":
        print 'Pokedex Entry '+str(210)+""
    elif pokemon == "Quilfish":
        print 'Pokedex Entry '+str(211)+""
    elif pokemon == "Scizor":
        print 'Pokedex Entry '+str(212)+""
    elif pokemon == "Shuckle":
        print 'Pokedex Entry '+str(213)+""
    elif pokemon == "Heracross":
        print 'Pokedex Entry '+str(214)+""
    elif pokemon == "Sneasel":
        print 'Pokedex Entry '+str(215)+""
    elif pokemon == "Teddiursa":
        print 'Pokedex Entry '+str(216)+""
    elif pokemon == "Ursaring":
        print 'Pokedex Entry '+str(217)+""
    elif pokemon == "Slugma":
        print 'Pokedex Entry '+str(218)+""
    elif pokemon == "Magcargo":
        print 'Pokedex Entry '+str(219)+""
    elif pokemon == "Swinub":
        print 'Pokedex Entry '+str(220)+""
    elif pokemon == "Piloswine":
        print 'Pokedex Entry '+str(221)+""
    elif pokemon == "Corsola":
        print 'Pokedex Entry '+str(222)+""
    elif pokemon == "Remoraid":
        print 'Pokedex Entry '+str(223)+""
    elif pokemon == "Octillery":
        print 'Pokedex Entry '+str(224)+""
    elif pokemon == "Delibird":
        print 'Pokedex Entry '+str(225)+""
    elif pokemon == "Mantine":
        print 'Pokedex Entry '+str(226)+""
    elif pokemon == "Skarmory":
        print 'Pokedex Entry '+str(227)+""
    elif pokemon == "Houndour":
        print 'Pokedex Entry '+str(228)+""
    elif pokemon == "Houndoom":
        print 'Pokedex Entry '+str(229)+""
    elif pokemon == "Kingdra":
        print 'Pokedex Entry '+str(230)+""
    elif pokemon == "Phanpy":
        print 'Pokedex Entry '+str(231)+""
    elif pokemon == "Donphan":
        print 'Pokedex Entry '+str(232)+""
    elif pokemon == "Porygon":
        print 'Pokedex Entry '+str(233)+""
    elif pokemon == "Stantler":
        print 'Pokedex Entry '+str(234)+""
    elif pokemon == "Smeargle":
        print 'Pokedex Entry '+str(235)+""
    elif pokemon == "Tyrogue":
        print 'Pokedex Entry '+str(236)+""
    elif pokemon == "Hitmontop":
        print 'Pokedex Entry '+str(237)+""
    elif pokemon == "Smoochum":
        print 'Pokedex Entry '+str(238)+""
    elif pokemon == "Elekid":
        print 'Pokedex Entry '+str(239)+""
    elif pokemon == "Magby":
        print 'Pokedex Entry '+str(240)+""
    elif pokemon == "Miltank":
        print 'Pokedex Entry '+str(241)+""
    elif pokemon == "Blissey":
        print 'Pokedex Entry '+str(242)+""
    elif pokemon == "Raikou":
        print 'Pokedex Entry '+str(243)+""
    elif pokemon == "Entei":
        print 'Pokedex Entry '+str(244)+""
    elif pokemon == "Suicune":
        print 'Pokedex Entry '+str(245)+""
    elif pokemon == "Larvitar":
        print 'Pokedex Entry '+str(246)+""
    elif pokemon == "Pupitar":
        print 'Pokedex Entry '+str(247)+""
    elif pokemon == "Tyranitar":
        print 'Pokedex Entry '+str(248)+""
    elif pokemon == "Lugia":
        print 'Pokedex Entry '+str(249)+""
    elif pokemon == "Ho-Oh":
        print 'Pokedex Entry '+str(250)+""
    elif pokemon == "Celebi":
        print 'Pokedex Entry '+str(251)+""
    elif pokemon == "Treecko":
        print 'Pokedex Entry '+str(252)+""
    elif pokemon == "Grovyle":
        print 'Pokedex Entry '+str(253)+""
    elif pokemon == "Sceptile":
        print 'Pokedex Entry '+str(254)+""
    elif pokemon == "Torchic":
        print 'Pokedex Entry '+str(255)+""
    elif pokemon == "Combusken":
        print 'Pokedex Entry '+str(256)+""
    elif pokemon == "Blaziken":
        print 'Pokedex Entry '+str(257)+""
    elif pokemon == "Mudkip":
        print 'Pokedex Entry '+str(258)+""
    elif pokemon == "Marshtomp":
        print 'Pokedex Entry '+str(259)+""
    elif pokemon == "Swampert":
        print 'Pokedex Entry '+str(260)+""
    elif pokemon == "Poochyena":
        print 'Pokedex Entry '+str(261)+""
    elif pokemon == "Mightyena":
        print 'Pokedex Entry '+str(262)+""
    elif pokemon == "Zigzagoon":
        print 'Pokedex Entry '+str(263)+""
    elif pokemon == "Linoone":
        print 'Pokedex Entry '+str(264)+""
    elif pokemon == "Wurmple":
        print 'Pokedex Entry '+str(265)+""
    elif pokemon == "Silcoon":
        print 'Pokedex Entry '+str(266)+""
    elif pokemon == "Beautifly":
        print 'Pokedex Entry '+str(267)+""
    elif pokemon == "Cascoon":
        print 'Pokedex Entry '+str(268)+""
    elif pokemon == "Dustox":
        print 'Pokedex Entry '+str(269)+""
    elif pokemon == "Lotad":
        print 'Pokedex Entry '+str(270)+""
    elif pokemon == "Lombre":
        print 'Pokedex Entry '+str(271)+""
    elif pokemon == "Ludicolo":
        print 'Pokedex Entry '+str(272)+""
    elif pokemon == "Seedot":
        print 'Pokedex Entry '+str(273)+""
    elif pokemon == "Nuzleaf":
        print 'Pokedex Entry '+str(274)+""
    elif pokemon == "Shiftry":
        print 'Pokedex Entry '+str(275)+""
    elif pokemon == "Taillow":
        print 'Pokedex Entry '+str(276)+""
    elif pokemon == "Swellow":
        print 'Pokedex Entry '+str(277)+""
    elif pokemon == "Wingull":
        print 'Pokedex Entry '+str(278)+""
    elif pokemon == "Pelipper":
        print 'Pokedex Entry '+str(279)+""
    elif pokemon == "Ralts":
        print 'Pokedex Entry '+str(280)+""
    elif pokemon == "Kirlia":
        print 'Pokedex Entry '+str(281)+""
    elif pokemon == "Gardevoir":
        print 'Pokedex Entry '+str(282)+""
    elif pokemon == "Surskit":
        print 'Pokedex Entry '+str(283)+""
    elif pokemon == "Masquerain":
        print 'Pokedex Entry '+str(284)+""
    elif pokemon == "Shroomish":
        print 'Pokedex Entry '+str(285)+""
    elif pokemon == "Breloom":
        print 'Pokedex Entry '+str(286)+""
    elif pokemon == "Slakoth":
        print 'Pokedex Entry '+str(287)+""
    elif pokemon == "Vigoroth":
        print 'Pokedex Entry '+str(288)+""
    elif pokemon == "Slaking":
        print 'Pokedex Entry '+str(289)+""
    elif pokemon == "Nincada":
        print 'Pokedex Entry '+str(290)+""
    elif pokemon == "Ninjask":
        print 'Pokedex Entry '+str(291)+""
    elif pokemon == "Shedinja":
        print 'Pokedex Entry '+str(292)+""
    elif pokemon == "Whismur":
        print 'Pokedex Entry '+str(293)+""
    elif pokemon == "Loudred":
        print 'Pokedex Entry '+str(294)+""
    elif pokemon == "Exploud":
        print 'Pokedex Entry '+str(295)+""
    elif pokemon == "Makuhita":
        print 'Pokedex Entry '+str(296)+""
    elif pokemon == "Hariyama":
        print 'Pokedex Entry '+str(297)+""
    elif pokemon == "Azurill":
        print 'Pokedex Entry '+str(298)+""
    elif pokemon == "Nosepass":
        print 'Pokedex Entry '+str(299)+""
    elif pokemon == "Skitty":
        print 'Pokedex Entry '+str(300)+""
    elif pokemon == "Delcatty":
        print 'Pokedex Entry '+str(301)+""
    elif pokemon == "Sableye":
        print 'Pokedex Entry '+str(302)+""
    elif pokemon == "Mawile":
        print 'Pokedex Entry '+str(303)+""
    elif pokemon == "Aron":
        print 'Pokedex Entry '+str(304)+""
    elif pokemon == "Lairon":
        print 'Pokedex Entry '+str(305)+""
    elif pokemon == "Aggron":
        print 'Pokedex Entry '+str(306)+""
    elif pokemon == "Meditite":
        print 'Pokedex Entry '+str(307)+""
    elif pokemon == "Medicham":
        print 'Pokedex Entry '+str(308)+""
    elif pokemon == "Electrike":
        print 'Pokedex Entry '+str(309)+""
    elif pokemon == "Manectric":
        print 'Pokedex Entry '+str(310)+""
    elif pokemon == "Plusle":
        print 'Pokedex Entry '+str(311)+""
    elif pokemon == "Minun":
        print 'Pokedex Entry '+str(312)+""
    elif pokemon == "Volbeat":
        print 'Pokedex Entry '+str(313)+""
    elif pokemon == "Illumise":
        print 'Pokedex Entry '+str(314)+""
    elif pokemon == "Roselia":
        print 'Pokedex Entry '+str(315)+""
    elif pokemon == "Gulpin":
        print 'Pokedex Entry '+str(316)+""
    elif pokemon == "Swalot":
        print 'Pokedex Entry '+str(317)+""
    elif pokemon == "Carvanha":
        print 'Pokedex Entry '+str(318)+""
    elif pokemon == "Sharpedo":
        print 'Pokedex Entry '+str(319)+""
    elif pokemon == "Wailmer":
        print 'Pokedex Entry '+str(320)+""
    elif pokemon == "Wailord":
        print 'Pokedex Entry '+str(321)+""
    elif pokemon == "Numel":
        print 'Pokedex Entry '+str(322)+""
    elif pokemon == "Camerupt":
        print 'Pokedex Entry '+str(323)+""
    elif pokemon == "Torkoal":
        print 'Pokedex Entry '+str(324)+""
    elif pokemon == "Spoink":
        print 'Pokedex Entry '+str(325)+""
    elif pokemon == "Grumpig":
        print 'Pokedex Entry '+str(326)+""
    elif pokemon == "Spinda":
        print 'Pokedex Entry '+str(327)+""
    elif pokemon == "Trapinch":
        print 'Pokedex Entry '+str(328)+""
    elif pokemon == "Vibrava":
        print 'Pokedex Entry '+str(329)+""
    elif pokemon == "Flygon":
        print 'Pokedex Entry '+str(330)+""
    elif pokemon == "Cacnea":
        print 'Pokedex Entry '+str(331)+""
    elif pokemon == "Cacturne":
        print 'Pokedex Entry '+str(332)+""
    elif pokemon == "Swablu":
        print 'Pokedex Entry '+str(333)+""
    elif pokemon == "Altaria":
        print 'Pokedex Entry '+str(334)+""
    elif pokemon == "Zangoose":
        print 'Pokedex Entry '+str(335)+""
    elif pokemon == "Seviper":
        print 'Pokedex Entry '+str(336)+""
    elif pokemon == "Lunatone":
        print 'Pokedex Entry '+str(337)+""
    elif pokemon == "Solrock":
        print 'Pokedex Entry '+str(338)+""
    elif pokemon == "Barboach":
        print 'Pokedex Entry '+str(339)+""
    elif pokemon == "Whiscash":
        print 'Pokedex Entry '+str(340)+""
    elif pokemon == "Corphish":
        print 'Pokedex Entry '+str(341)+""
    elif pokemon == "Crawdaunt":
        print 'Pokedex Entry '+str(342)+""
    elif pokemon == "Baltoy":
        print 'Pokedex Entry '+str(343)+""
    elif pokemon == "Claydol":
        print 'Pokedex Entry '+str(344)+""
    elif pokemon == "Lileep":
        print 'Pokedex Entry '+str(345)+""
    elif pokemon == "Cradily":
        print 'Pokedex Entry '+str(346)+""
    elif pokemon == "Anorith":
        print 'Pokedex Entry '+str(347)+""
    elif pokemon == "Armaldo":
        print 'Pokedex Entry '+str(348)+""
    elif pokemon == "Feebas":
        print 'Pokedex Entry '+str(349)+""
    elif pokemon == "Milotic":
        print 'Pokedex Entry '+str(350)+""
    elif pokemon == "Castform":
        print 'Pokedex Entry '+str(351)+""
    elif pokemon == "Kecleon":
        print 'Pokedex Entry '+str(352)+""
    elif pokemon == "Shuppet":
        print 'Pokedex Entry '+str(353)+""
    elif pokemon == "Banette":
        print 'Pokedex Entry '+str(354)+""
    elif pokemon == "Duskull":
        print 'Pokedex Entry '+str(355)+""
    elif pokemon == "Dusclops":
        print 'Pokedex Entry '+str(356)+""
    elif pokemon == "Tropius":
        print 'Pokedex Entry '+str(357)+""
    elif pokemon == "Chimecho":
        print 'Pokedex Entry '+str(358)+""
    elif pokemon == "Absol":
        print 'Pokedex Entry '+str(359)+""
    elif pokemon == "Wynaut":
        print 'Pokedex Entry '+str(360)+""
    elif pokemon == "Snorunt":
        print 'Pokedex Entry '+str(361)+""
    elif pokemon == "Glalie":
        print 'Pokedex Entry '+str(362)+""
    elif pokemon == "Spheal":
        print 'Pokedex Entry '+str(363)+""
    elif pokemon == "Sealeo":
        print 'Pokedex Entry '+str(364)+""
    elif pokemon == "Walrein":
        print 'Pokedex Entry '+str(365)+""
    elif pokemon == "Clamperl":
        print 'Pokedex Entry '+str(366)+""
    elif pokemon == "Huntail":
        print 'Pokedex Entry '+str(367)+""
    elif pokemon == "Gorebyss":
        print 'Pokedex Entry '+str(368)+""
    elif pokemon == "Relicanth":
        print 'Pokedex Entry '+str(369)+""
    elif pokemon == "Luvdisc":
        print 'Pokedex Entry '+str(370)+""
    elif pokemon == "Bagon":
        print 'Pokedex Entry '+str(371)+""
    elif pokemon == "Shelgon":
        print 'Pokedex Entry '+str(372)+""
    elif pokemon == "Salamence":
        print 'Pokedex Entry '+str(373)+""
    elif pokemon == "Beldum":
        print 'Pokedex Entry '+str(374)+""
    elif pokemon == "Metang":
        print 'Pokedex Entry '+str(375)+""
    elif pokemon == "Metagross":
        print 'Pokedex Entry '+str(376)+""
    elif pokemon == "Regirock":
        print 'Pokedex Entry '+str(377)+""
    elif pokemon == "Regice":
        print 'Pokedex Entry '+str(378)+""
    elif pokemon == "Registeel":
        print 'Pokedex Entry '+str(379)+""
    elif pokemon == "Latias":
        print 'Pokedex Entry '+str(380)+""
    elif pokemon == "Latios":
        print 'Pokedex Entry '+str(381)+""
    elif pokemon == "Kyogre":
        print 'Pokedex Entry '+str(382)+""
    elif pokemon == "Groudon":
        print 'Pokedex Entry '+str(383)+""
    elif pokemon == "Rayquaza":
        print 'Pokedex Entry '+str(384)+""
    elif pokemon == "Jirachi":
        print 'Pokedex Entry '+str(385)+""
    elif pokemon == "Deoxys":
        print 'Pokedex Entry '+str(386)+""
    elif pokemon == "Turtwig":
        print 'Pokedex Entry '+str(387)+""
    elif pokemon == "Grotle":
        print 'Pokedex Entry '+str(388)+""
    elif pokemon == "Torterra":
        print 'Pokedex Entry '+str(389)+""
    elif pokemon == "Chimchar":
        print 'Pokedex Entry '+str(390)+""
    elif pokemon == "Monferno":
        print 'Pokedex Entry '+str(391)+""
    elif pokemon == "Infernape":
        print 'Pokedex Entry '+str(392)+""
    elif pokemon == "Piplup":
        print 'Pokedex Entry '+str(393)+""
    elif pokemon == "Primplup":
        print 'Pokedex Entry '+str(394)+""
    elif pokemon == "Empoleon":
        print 'Pokedex Entry '+str(395)+""
    elif pokemon == "Starly":
        print 'Pokedex Entry '+str(396)+""
    elif pokemon == "Staravia":
        print 'Pokedex Entry '+str(397)+""
    elif pokemon == "Staraptor":
        print 'Pokedex Entry '+str(398)+""
    elif pokemon == "Bidoof":
        print 'Pokedex Entry '+str(399)+""
    elif pokemon == "Bibarel":
        print 'Pokedex Entry '+str(400)+""
    elif pokemon == "Kricketot":
        print 'Pokedex Entry '+str(401)+""
    elif pokemon == "Kricketune":
        print 'Pokedex Entry '+str(402)+""
    elif pokemon == "Shinx":
        print 'Pokedex Entry '+str(403)+""
    elif pokemon == "Luxio":
        print 'Pokedex Entry '+str(404)+""
    elif pokemon == "Luxray":
        print 'Pokedex Entry '+str(405)+""
    elif pokemon == "Budew":
        print 'Pokedex Entry '+str(406)+""
    elif pokemon == "Roserade":
        print 'Pokedex Entry '+str(407)+""
    elif pokemon == "Cranidos":
        print 'Pokedex Entry '+str(408)+""
    elif pokemon == "Rampardos":
        print 'Pokedex Entry '+str(409)+""
    elif pokemon == "Shieldon":
        print 'Pokedex Entry '+str(410)+""
    elif pokemon == "Bastiodon":
        print 'Pokedex Entry '+str(411)+""
    elif pokemon == "Burmy":
        print 'Pokedex Entry '+str(412)+""
    elif pokemon == "Wormadam":
        print 'Pokedex Entry '+str(413)+""
    elif pokemon == "Mothim":
        print 'Pokedex Entry '+str(414)+""
    elif pokemon == "Combee":
        print 'Pokedex Entry '+str(415)+""
    elif pokemon == "Vespiquen":
        print 'Pokedex Entry '+str(416)+""
    elif pokemon == "Pachirisu":
        print 'Pokedex Entry '+str(417)+""
    elif pokemon == "Buizel":
        print 'Pokedex Entry '+str(418)+""
    elif pokemon == "Floatzel":
        print 'Pokedex Entry '+str(419)+""
    elif pokemon == "Cherubi":
        print 'Pokedex Entry '+str(420)+""
    elif pokemon == "Cherrim":
        print 'Pokedex Entry '+str(421)+""
    elif pokemon == "Shellos":
        print 'Pokedex Entry '+str(422)+""
    elif pokemon == "Gastrodon":
        print 'Pokedex Entry '+str(423)+""
    elif pokemon == "Ambipom":
        print 'Pokedex Entry '+str(424)+""
    elif pokemon == "Drifloon":
        print 'Pokedex Entry '+str(425)+""
    elif pokemon == "Drifblim":
        print 'Pokedex Entry '+str(426)+""
    elif pokemon == "Buneary":
        print 'Pokedex Entry '+str(427)+""
    elif pokemon == "Lopunny":
        print 'Pokedex Entry '+str(428)+""
    elif pokemon == "Mismagius":
        print 'Pokedex Entry '+str(429)+""
    elif pokemon == "Honchkrow":
        print 'Pokedex Entry '+str(430)+""
    elif pokemon == "Glameow":
        print 'Pokedex Entry '+str(431)+""
    elif pokemon == "Purugly":
        print 'Pokedex Entry '+str(432)+""
    elif pokemon == "Chingling":
        print 'Pokedex Entry '+str(433)+""
    elif pokemon == "Stunky":
        print 'Pokedex Entry '+str(434)+""
    elif pokemon == "Skuntank":
        print 'Pokedex Entry '+str(435)+""
    elif pokemon == "Bronzor":
        print 'Pokedex Entry '+str(436)+""
    elif pokemon == "Bronzong":
        print 'Pokedex Entry '+str(437)+""
    elif pokemon == "Bonsly":
        print 'Pokedex Entry '+str(438)+""
    elif pokemon == "Mime Jr.":
        print 'Pokedex Entry '+str(439)+""
    elif pokemon == "Happiny":
        print 'Pokedex Entry '+str(440)+""
    elif pokemon == "Chatot":
        print 'Pokedex Entry '+str(441)+""
    elif pokemon == "Spiritomb":
        print 'Pokedex Entry '+str(442)+""
    elif pokemon == "Gible":
        print 'Pokedex Entry '+str(443)+""
    elif pokemon == "Gabite":
        print 'Pokedex Entry '+str(444)+""
    elif pokemon == "Garchomp":
        print 'Pokedex Entry '+str(445)+""
    elif pokemon == "Munchlax":
        print 'Pokedex Entry '+str(446)+""
    elif pokemon == "Riolu":
        print 'Pokedex Entry '+str(447)+""
    elif pokemon == "Lucario":
        print 'Pokedex Entry '+str(448)+""
    elif pokemon == "Hippopotas":
        print 'Pokedex Entry '+str(449)+""
    elif pokemon == "Hippowdon":
        print 'Pokedex Entry '+str(450)+""
    elif pokemon == "Skorupi":
        print 'Pokedex Entry '+str(451)+""
    elif pokemon == "Drapion":
        print 'Pokedex Entry '+str(452)+""
    elif pokemon == "Croagunk":
        print 'Pokedex Entry '+str(453)+""
    elif pokemon == "Toxicroak":
        print 'Pokedex Entry '+str(454)+""
    elif pokemon == "Carnivine":
        print 'Pokedex Entry '+str(455)+""
    elif pokemon == "Finneon":
        print 'Pokedex Entry '+str(456)+""
    elif pokemon == "Lumineon":
        print 'Pokedex Entry '+str(457)+""
    elif pokemon == "Mantyke":
        print 'Pokedex Entry '+str(458)+""
    elif pokemon == "Snover":
        print 'Pokedex Entry '+str(459)+""
    elif pokemon == "Abomasnow":
        print 'Pokedex Entry '+str(460)+""
    elif pokemon == "Weavile":
        print 'Pokedex Entry '+str(461)+""
    elif pokemon == "Magnezone":
        print 'Pokedex Entry '+str(462)+""
    elif pokemon == "Lickilicky":
        print 'Pokedex Entry '+str(463)+""
    elif pokemon == "Rhyperior":
        print 'Pokedex Entry '+str(464)+""
    elif pokemon == "Tangrowth":
        print 'Pokedex Entry '+str(465)+""
    elif pokemon == "Electivire":
        print 'Pokedex Entry '+str(466)+""
    elif pokemon == "Magmortar":
        print 'Pokedex Entry '+str(467)+""
    elif pokemon == "Togekiss":
        print 'Pokedex Entry '+str(468)+""
    elif pokemon == "Yanmega":
        print 'Pokedex Entry '+str(469)+""
    elif pokemon == "Leafeon":
        print 'Pokedex Entry '+str(470)+""
    elif pokemon == "Glaceon":
        print 'Pokedex Entry '+str(471)+""
    elif pokemon == "Gliscor":
        print 'Pokedex Entry '+str(472)+""
    elif pokemon == "Mamoswine":
        print 'Pokedex Entry '+str(473)+""
    elif pokemon == "Porygon-Z":
        print 'Pokedex Entry '+str(474)+""
    elif pokemon == "Gallade":
        print 'Pokedex Entry '+str(475)+""
    elif pokemon == "Probopass":
        print 'Pokedex Entry '+str(476)+""
    elif pokemon == "Dusknoir":
        print 'Pokedex Entry '+str(477)+""
    elif pokemon == "Froslass":
        print 'Pokedex Entry '+str(478)+""
    elif pokemon == "Rotom":
        print 'Pokedex Entry '+str(479)+""
    elif pokemon == "Uxie":
        print 'Pokedex Entry '+str(480)+""
    elif pokemon == "Mesprit":
        print 'Pokedex Entry '+str(481)+""
    elif pokemon == "Azelf":
        print 'Pokedex Entry '+str(482)+""
    elif pokemon == "Dialga":
        print 'Pokedex Entry '+str(483)+""
    elif pokemon == "Palkia":
        print 'Pokedex Entry '+str(484)+""
    elif pokemon == "Heatran":
        print 'Pokedex Entry '+str(485)+""
    elif pokemon == "Regigigas":
        print 'Pokedex Entry '+str(486)+""
    elif pokemon == "Giratina":
        print 'Pokedex Entry '+str(487)+""
    elif pokemon == "Cresselia":
        print 'Pokedex Entry '+str(488)+""
    elif pokemon == "Phione":
        print 'Pokedex Entry '+str(489)+""
    elif pokemon == "Manaphy":
        print 'Pokedex Entry '+str(490)+""
    elif pokemon == "Darkrai":
        print 'Pokedex Entry '+str(491)+""
    elif pokemon == "Shaymin":
        print 'Pokedex Entry '+str(492)+""
    elif pokemon == "Arceus":
        print 'Pokedex Entry '+str(493)+""
    elif pokemon == "Victini":
        print 'Pokedex Entry '+str(494)+""
    elif pokemon == "Snivy":
        print 'Pokedex Entry '+str(495)+""
    elif pokemon == "Servine":
        print 'Pokedex Entry '+str(496)+""
    elif pokemon == "Serperior":
        print 'Pokedex Entry '+str(497)+""
    elif pokemon == "Tepig":
        print 'Pokedex Entry '+str(498)+""
    elif pokemon == "Pignite":
        print 'Pokedex Entry '+str(499)+""
    elif pokemon == "Emboar":
        print 'Pokedex Entry '+str(500)+""
    elif pokemon == "Oshawott":
        print 'Pokedex Entry '+str(501)+""
    elif pokemon == "Dewott":
        print 'Pokedex Entry '+str(502)+""
    elif pokemon == "Samurott":
        print 'Pokedex Entry '+str(503)+""
    elif pokemon == "Patrat":
        print 'Pokedex Entry '+str(504)+""
    elif pokemon == "Watchog":
        print 'Pokedex Entry '+str(505)+""
    elif pokemon == "Lillipup":
        print 'Pokedex Entry '+str(506)+""
    elif pokemon == "Herdier":
        print 'Pokedex Entry '+str(507)+""
    elif pokemon == "Stoutland":
        print 'Pokedex Entry '+str(508)+""
    elif pokemon == "Purrloin":
        print 'Pokedex Entry '+str(509)+""
    elif pokemon == "Liepard":
        print 'Pokedex Entry '+str(510)+""
    elif pokemon == "Pansage":
        print 'Pokedex Entry '+str(511)+""
    elif pokemon == "Simisage":
        print 'Pokedex Entry '+str(512)+""
    elif pokemon == "Pansear":
        print 'Pokedex Entry '+str(513)+""
    elif pokemon == "Simisear":
        print 'Pokedex Entry '+str(514)+""
    elif pokemon == "Panpour":
        print 'Pokedex Entry '+str(515)+""
    elif pokemon == "Simipour":
        print 'Pokedex Entry '+str(516)+""
    elif pokemon == "Munna":
        print 'Pokedex Entry '+str(517)+""
    elif pokemon == "Musharna":
        print 'Pokedex Entry '+str(518)+""
    elif pokemon == "Pidove":
        print 'Pokedex Entry '+str(519)+""
    elif pokemon == "Tranquill":
        print 'Pokedex Entry '+str(520)+""
    elif pokemon == "Unfezant":
        print 'Pokedex Entry '+str(521)+""
    elif pokemon == "Blitzle":
        print 'Pokedex Entry '+str(522)+""
    elif pokemon == "Zebstrika":
        print 'Pokedex Entry '+str(523)+""
    elif pokemon == "Roggenrola":
        print 'Pokedex Entry '+str(524)+""
    elif pokemon == "Boldore":
        print 'Pokedex Entry '+str(525)+""
    elif pokemon == "Gigalith":
        print 'Pokedex Entry '+str(526)+""
    elif pokemon == "Woobat":
        print 'Pokedex Entry '+str(527)+""
    elif pokemon == "Swoobat":
        print 'Pokedex Entry '+str(528)+""
    elif pokemon == "Drilbur":
        print 'Pokedex Entry '+str(529)+""
    elif pokemon == "Excadrill":
        print 'Pokedex Entry '+str(530)+""
    elif pokemon == "Audino":
        print 'Pokedex Entry '+str(531)+""
    elif pokemon == "Timburr":
        print 'Pokedex Entry '+str(532)+""
    elif pokemon == "Gurdurr":
        print 'Pokedex Entry '+str(533)+""
    elif pokemon == "Conkeldurr":
        print 'Pokedex Entry '+str(534)+""
    elif pokemon == "Tympole":
        print 'Pokedex Entry '+str(535)+""
    elif pokemon == "Palpitoad":
        print 'Pokedex Entry '+str(536)+""
    elif pokemon == "Seismitoad":
        print 'Pokedex Entry '+str(537)+""
    elif pokemon == "Throh":
        print 'Pokedex Entry '+str(538)+""
    elif pokemon == "Sawk":
        print 'Pokedex Entry '+str(539)+""
    elif pokemon == "Sewaddle":
        print 'Pokedex Entry '+str(540)+""
    elif pokemon == "Swadloon":
        print 'Pokedex Entry '+str(541)+""
    elif pokemon == "Levanny":
        print 'Pokedex Entry '+str(542)+""
    elif pokemon == "Venipede":
        print 'Pokedex Entry '+str(543)+""
    elif pokemon == "Whirlipede":
        print 'Pokedex Entry '+str(544)+""
    elif pokemon == "Scolipede":
        print 'Pokedex Entry '+str(545)+""
    elif pokemon == "Cottonee":
        print 'Pokedex Entry '+str(546)+""
    elif pokemon == "Whimsicott":
        print 'Pokedex Entry '+str(547)+""
    elif pokemon == "Petilil":
        print 'Pokedex Entry '+str(548)+""
    elif pokemon == "Lilligant":
        print 'Pokedex Entry '+str(549)+""
    elif pokemon == "Basculin":
        print 'Pokedex Entry '+str(550)+""
    elif pokemon == "Sandile":
        print 'Pokedex Entry '+str(551)+""
    elif pokemon == "Krokorok":
        print 'Pokedex Entry '+str(552)+""
    elif pokemon == "Krookodile":
        print 'Pokedex Entry '+str(553)+""
    elif pokemon == "Darumaka":
        print 'Pokedex Entry '+str(554)+""
    elif pokemon == "Darmanitan":
        print 'Pokedex Entry '+str(555)+""
    elif pokemon == "Maractus":
        print 'Pokedex Entry '+str(556)+""
    elif pokemon == "Dwebble":
        print 'Pokedex Entry '+str(557)+""
    elif pokemon == "Crustle":
        print 'Pokedex Entry '+str(558)+""
    elif pokemon == "Scraggy":
        print 'Pokedex Entry '+str(559)+""
    elif pokemon == "Scrafty":
        print 'Pokedex Entry '+str(560)+""
    elif pokemon == "Sigilyph":
        print 'Pokedex Entry '+str(561)+""
    elif pokemon == "Yamask":
        print 'Pokedex Entry '+str(562)+""
    elif pokemon == "Cofagrigus":
        print 'Pokedex Entry '+str(563)+""
    elif pokemon == "Tirtouga":
        print 'Pokedex Entry '+str(564)+""
    elif pokemon == "Carracosta":
        print 'Pokedex Entry '+str(565)+""
    elif pokemon == "Archen":
        print 'Pokedex Entry '+str(566)+""
    elif pokemon == "Archeops":
        print 'Pokedex Entry '+str(567)+""
    elif pokemon == "Trubbish":
        print 'Pokedex Entry '+str(568)+""
    elif pokemon == "Garbodor":
        print 'Pokedex Entry '+str(569)+""
    elif pokemon == "Zorua":
        print 'Pokedex Entry '+str(570)+""
    elif pokemon == "Zoroark":
        print 'Pokedex Entry '+str(571)+""
    elif pokemon == "Minccino":
        print 'Pokedex Entry '+str(572)+""
    elif pokemon == "Cinccino":
        print 'Pokedex Entry '+str(573)+""
    elif pokemon == "Gothita":
        print 'Pokedex Entry '+str(574)+""
    elif pokemon == "Gothorita":
        print 'Pokedex Entry '+str(575)+""
    elif pokemon == "Gothitelle":
        print 'Pokedex Entry '+str(576)+""
    elif pokemon == "Solosis":
        print 'Pokedex Entry '+str(577)+""
    elif pokemon == "Duosion":
        print 'Pokedex Entry '+str(578)+""
    elif pokemon == "Reuniclus":
        print 'Pokedex Entry '+str(579)+""
    elif pokemon == "Ducklett":
        print 'Pokedex Entry '+str(580)+""
    elif pokemon == "Swanna":
        print 'Pokedex Entry '+str(581)+""
    elif pokemon == "Valillite":
        print 'Pokedex Entry '+str(582)+""
    elif pokemon == "Vanillish":
        print 'Pokedex Entry '+str(583)+""
    elif pokemon == "Vanilluxe":
        print 'Pokedex Entry '+str(584)+""
    elif pokemon == "Deerling":
        print 'Pokedex Entry '+str(585)+""
    elif pokemon == "Sawsbuck":
        print 'Pokedex Entry '+str(586)+""
    elif pokemon == "Emolga":
        print 'Pokedex Entry '+str(587)+""
    elif pokemon == "Karrablast":
        print 'Pokedex Entry '+str(588)+""
    elif pokemon == "Escavalier":
        print 'Pokedex Entry '+str(589)+""
    elif pokemon == "Foongus":
        print 'Pokedex Entry '+str(590)+""
    elif pokemon == "Amoonguss":
        print 'Pokedex Entry '+str(591)+""
    elif pokemon == "Frillish":
        print 'Pokedex Entry '+str(592)+""
    elif pokemon == "Jellicent":
        print 'Pokedex Entry '+str(593)+""
    elif pokemon == "Alomomola":
        print 'Pokedex Entry '+str(594)+""
    elif pokemon == "Joltik":
        print 'Pokedex Entry '+str(595)+""
    elif pokemon == "Galvantula":
        print 'Pokedex Entry '+str(596)+""
    elif pokemon == "Ferroseed":
        print 'Pokedex Entry '+str(597)+""
    elif pokemon == "Ferrothorn":
        print 'Pokedex Entry '+str(598)+""
    elif pokemon == "Klink":
        print 'Pokedex Entry '+str(599)+""
    elif pokemon == "Klang":
        print 'Pokedex Entry '+str(600)+""
    elif pokemon == "Klinklang":
        print 'Pokedex Entry '+str(601)+""
    elif pokemon == "Tynamo":
        print 'Pokedex Entry '+str(602)+""
    elif pokemon == "Eelektrik":
        print 'Pokedex Entry '+str(603)+""
    elif pokemon == "Eelektross":
        print 'Pokedex Entry '+str(604)+""
    elif pokemon == "Elgyem":
        print 'Pokedex Entry '+str(605)+""
    elif pokemon == "Beheeyem":
        print 'Pokedex Entry '+str(606)+""
    elif pokemon == "Litwick":
        print 'Pokedex Entry '+str(607)+""
    elif pokemon == "Lampent":
        print 'Pokedex Entry '+str(608)+""
    elif pokemon == "Chandelure":
        print 'Pokedex Entry '+str(609)+""
    elif pokemon == "Axew":
        print 'Pokedex Entry '+str(610)+""
    elif pokemon == "Fraxure":
        print 'Pokedex Entry '+str(611)+""
    elif pokemon == "Haxorus":
        print 'Pokedex Entry '+str(612)+""
    elif pokemon == "Cubchoo":
        print 'Pokedex Entry '+str(613)+""
    elif pokemon == "Beartic":
        print 'Pokedex Entry '+str(614)+""
    elif pokemon == "Cryogonal":
        print 'Pokedex Entry '+str(615)+""
    elif pokemon == "Shelmet":
        print 'Pokedex Entry '+str(616)+""
    elif pokemon == "Accelgor":
        print 'Pokedex Entry '+str(617)+""
    elif pokemon == "Stunfisk":
        print 'Pokedex Entry '+str(618)+""
    elif pokemon == "Mienfoo":
        print 'Pokedex Entry '+str(619)+""
    elif pokemon == "Mienshao":
        print 'Pokedex Entry '+str(620)+""
    elif pokemon == "Druddigon":
        print 'Pokedex Entry '+str(621)+""
    elif pokemon == "Golett":
        print 'Pokedex Entry '+str(622)+""
    elif pokemon == "Golurk":
        print 'Pokedex Entry '+str(623)+""
    elif pokemon == "Pawniard":
        print 'Pokedex Entry '+str(624)+""
    elif pokemon == "Bisharp":
        print 'Pokedex Entry '+str(625)+""
    elif pokemon == "Bouffalant":
        print 'Pokedex Entry '+str(626)+""
    elif pokemon == "Rufflet":
        print 'Pokedex Entry '+str(627)+""
    elif pokemon == "Braviary":
        print 'Pokedex Entry '+str(628)+""
    elif pokemon == "Vullaby":
        print 'Pokedex Entry '+str(629)+""
    elif pokemon == "Mandibuzz":
        print 'Pokedex Entry '+str(630)+""
    elif pokemon == "Heatmor":
        print 'Pokedex Entry '+str(631)+""
    elif pokemon == "Durant":
        print 'Pokedex Entry '+str(632)+""
    elif pokemon == "Deino":
        print 'Pokedex Entry '+str(633)+""
    elif pokemon == "Zweilous":
        print 'Pokedex Entry '+str(634)+""
    elif pokemon == "Hydreigon":
        print 'Pokedex Entry '+str(635)+""
    elif pokemon == "Larvesta":
        print 'Pokedex Entry '+str(636)+""
    elif pokemon == "Volcarona":
        print 'Pokedex Entry '+str(637)+""
    elif pokemon == "Cobalion":
        print 'Pokedex Entry '+str(638)+""
    elif pokemon == "Terrakion":
        print 'Pokedex Entry '+str(639)+""
    elif pokemon == "Virizion":
        print 'Pokedex Entry '+str(640)+""
    elif pokemon == "Tornadus":
        print 'Pokedex Entry '+str(641)+""
    elif pokemon == "Thundurus":
        print 'Pokedex Entry '+str(642)+""
    elif pokemon == "Reshiram":
        print 'Pokedex Entry '+str(643)+""
    elif pokemon == "Zekrom":
        print 'Pokedex Entry '+str(644)+""
    elif pokemon == "Landorus":
        print 'Pokedex Entry '+str(645)+""
    elif pokemon == "Kyurem":
        print 'Pokedex Entry '+str(646)+""
    elif pokemon == "Keldeo":
        print 'Pokedex Entry '+str(647)+""
    elif pokemon == "Meloetta":
        print 'Pokedex Entry '+str(648)+""
    elif pokemon == "Genesect":
        print 'Pokedex Entry '+str(649)+""
    elif pokemon == "Chespin":
        print 'Pokedex Entry '+str(650)+""
    elif pokemon == "Quilladin":
        print 'Pokedex Entry '+str(651)+""
    elif pokemon == "Chesnaught":
        print 'Pokedex Entry '+str(652)+""
    elif pokemon == "Fennekin":
        print 'Pokedex Entry '+str(653)+""
    elif pokemon == "Braixen":
        print 'Pokedex Entry '+str(654)+""
    elif pokemon == "Delphox":
        print 'Pokedex Entry '+str(655)+""
    elif pokemon == "Froakie":
        print 'Pokedex Entry '+str(656)+""
    elif pokemon == "Frogadier":
        print 'Pokedex Entry '+str(657)+""
    elif pokemon == "Greninja":
        print 'Pokedex Entry '+str(658)+""
    elif pokemon == "Bunnelby":
        print 'Pokedex Entry '+str(659)+""
    elif pokemon == "Diggersby":
        print 'Pokedex Entry '+str(660)+""
    elif pokemon == "Fletchling":
        print 'Pokedex Entry '+str(661)+""
    elif pokemon == "Fletchinder":
        print 'Pokedex Entry '+str(662)+""
    elif pokemon == "Talonflame":
        print 'Pokedex Entry '+str(663)+""
    elif pokemon == "Scatterbug":
        print 'Pokedex Entry '+str(664)+""
    elif pokemon == "Spewpa":
        print 'Pokedex Entry '+str(665)+""
    elif pokemon == "Vivillon":
        print 'Pokedex Entry '+str(666)+""
    elif pokemon == "Litleo":
        print 'Pokedex Entry '+str(667)+""
    elif pokemon == "Pyroar":
        print 'Pokedex Entry '+str(668)+""
    elif pokemon == "Flab"b"":
        print 'Pokedex Entry '+str(669)+""
    elif pokemon == "Floette":
        print 'Pokedex Entry '+str(670)+""
    elif pokemon == "Florges":
        print 'Pokedex Entry '+str(671)+""
    elif pokemon == "Skiddo":
        print 'Pokedex Entry '+str(672)+""
    elif pokemon == "Gogoat":
        print 'Pokedex Entry '+str(673)+""
    elif pokemon == "Pancham":
        print 'Pokedex Entry '+str(674)+""
    elif pokemon == "Pangoro":
        print 'Pokedex Entry '+str(675)+""
    elif pokemon == "Furfrou":
        print 'Pokedex Entry '+str(676)+""
    elif pokemon == "Espurr":
        print 'Pokedex Entry '+str(677)+""
    elif pokemon == "Meowstic":
        print 'Pokedex Entry '+str(678)+""
    elif pokemon == "Honedge":
        print 'Pokedex Entry '+str(679)+""
    elif pokemon == "Doublade":
        print 'Pokedex Entry '+str(680)+""
    elif pokemon == "Aegislash":
        print 'Pokedex Entry '+str(681)+""
    elif pokemon == "Spritzee":
        print 'Pokedex Entry '+str(682)+""
    elif pokemon == "Aromatisse":
        print 'Pokedex Entry '+str(683)+""
    elif pokemon == "Swirlix":
        print 'Pokedex Entry '+str(684)+""
    elif pokemon == "Slurpuff":
        print 'Pokedex Entry '+str(685)+""
    elif pokemon == "Inkay":
        print 'Pokedex Entry '+str(686)+""
    elif pokemon == "Malamar":
        print 'Pokedex Entry '+str(687)+""
    elif pokemon == "Binacle":
        print 'Pokedex Entry '+str(688)+""
    elif pokemon == "Barbaracle":
        print 'Pokedex Entry '+str(689)+""
    elif pokemon == "Skrelp":
        print 'Pokedex Entry '+str(690)+""
    elif pokemon == "Dragalge":
        print 'Pokedex Entry '+str(691)+""
    elif pokemon == "Clauncher":
        print 'Pokedex Entry '+str(692)+""
    elif pokemon == "Clawitzer":
        print 'Pokedex Entry '+str(693)+""
    elif pokemon == "Helioptile":
        print 'Pokedex Entry '+str(694)+""
    elif pokemon == "Heliolisk":
        print 'Pokedex Entry '+str(695)+""
    elif pokemon == "Tyrunt":
        print 'Pokedex Entry '+str(696)+""
    elif pokemon == "Tyrantrum":
        print 'Pokedex Entry '+str(697)+""
    elif pokemon == "Amaura":
        print 'Pokedex Entry '+str(698)+""
    elif pokemon == "Aurorus":
        print 'Pokedex Entry '+str(699)+""
    elif pokemon == "Sylveon":
        print 'Pokedex Entry '+str(700)+""
    elif pokemon == "Hawlucha":
        print 'Pokedex Entry '+str(701)+""
    elif pokemon == "Dedenne":
        print 'Pokedex Entry '+str(702)+""
    elif pokemon == "Carbink":
        print 'Pokedex Entry '+str(703)+""
    elif pokemon == "Goomy":
        print 'Pokedex Entry '+str(704)+""
    elif pokemon == "Sliggoo":
        print 'Pokedex Entry '+str(705)+""
    elif pokemon == "Goodra":
        print 'Pokedex Entry '+str(706)+""
    elif pokemon == "Klefki":
        print 'Pokedex Entry '+str(707)+""
    elif pokemon == "Phantump":
        print 'Pokedex Entry '+str(708)+""
    elif pokemon == "Trevenant":
        print 'Pokedex Entry '+str(709)+""
    elif pokemon == "Pumpkaboo":
        print 'Pokedex Entry '+str(710)+""
    elif pokemon == "Gourgeist":
        print 'Pokedex Entry '+str(711)+""
    elif pokemon == "Bergmite":
        print 'Pokedex Entry '+str(712)+""
    elif pokemon == "Avalugg":
        print 'Pokedex Entry '+str(713)+""
    elif pokemon == "Noibat":
        print 'Pokedex Entry '+str(714)+""
    elif pokemon == "Noivern":
        print 'Pokedex Entry '+str(715)+""
    elif pokemon == "Xerneas":
        print 'Pokedex Entry '+str(716)+""
    elif pokemon == "Yveltal":
        print 'Pokedex Entry '+str(717)+""
    elif pokemon == "Zygarde":
        print 'Pokedex Entry '+str(718)+""
    elif pokemon == "Diancie":
        print 'Pokedex Entry '+str(719)+""
    elif pokemon == "Hoopa":
        print 'Pokedex Entry '+str(720)+""
    elif pokemon == "Volcanion":
        print 'Pokedex Entry '+str(721)+""
    else:
        print "You have entered an unregistered name. Please try again."
    print ""
    searchanother = input("Would you like to search for another pokemon? ")
    if searchanother == True or searchanother == Yes or searchanother==yes:
        return pokemonnames()
    else:
        exit
