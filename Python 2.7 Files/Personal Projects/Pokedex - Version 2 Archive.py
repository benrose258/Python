def pokedex():
    pokemonlist = ["Bulbasaur","Ivysaur","Venasaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran(F)","Nidorina","Nidoqueen","Nidoran(M)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetails","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew","Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Quilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-Oh","Celebi","Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys","Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Primplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Wormadam","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime Jr.","Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Probopass","Dusknoir","Froslass","Rotom","Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina",
"Cresselia","Phione","Manaphy","Darkrai","Shaymin","Arceus","Victini","Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Valillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus","Thundurus","Reshiram","Zekrom","Landorus","Kyurem","Keldeo","Meloetta","Genesect","Chespin","Quilladin","Chesnaught","Fennekin","Braixen","Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa","Vivillon","Litleo","Pyroar","Flab�b�","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic","Honedge","Doublade","Aegislash","Spritzee","Aromatisse","Swirlix","Slurpuff","Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt","Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant","Pumpkaboo","Gourgeist","Bergmite","Avalugg","Noibat","Noivern","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Volcanion"]
    print "Dexter Version 2.0"
    print ""
    print "Search Pokemon by number: ('Search')"
    print "Search all Pokemon by number: ('Intervals')"
    print "Search by reigonal pokedex: ('Reigons')"
    whatfeature = input("Which of the above features would you like to use? ")
    if whatfeature == "Search":
        whichpokemon = input("Which pokemon are you looking for? (By number)")
        print "Pokedex Entry "+str(whichpokemon)+": "+str(pokemonlist[whichpokemon-1])
    elif whatfeature == "Reigons":
        whichreigon = input("Which reigon's pokedex would you like to view? ('Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos')")
        if whichreigon == "Kanto":
            currentpokemon = 1
            kantolist = pokemonlist[0:151]
            for index in kantolist:
                print "Kanto Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
        elif whichreigon == "Johto":
            currentpokemon = 1
            johtolist = pokemonlist[152:251]
            for index in johtolist:
                print "Johto Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
        elif whichreigon == "Hoenn":
            currentpokemon = 1
            hoennlist = pokemonlist[252:386]
            for index in hoennlist:
                print "Hoenn Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon=currentpokemon+1
        elif whichreigon == "Sinnoh":
            currentpokemon = 1
            sinnohlist = pokemonlist[387:493]
            for index in sinnohlist:
                print "Sinnoh Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon+1
        elif whichreigon == "Unova":
            currentpokemon = 0
            unovalist = pokemonlist[494:649]
            for index in unovalist:
                print "Unova Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon + 1
        elif whichreigon == "Kalos":
            currentpokemon = 1
            kaloslist = pokemonlist[650:]
            for index in kaloslist:
                print "Kalos Pokedex Entry "+str(currentpokemon)+": ",index
                currentpokemon = currentpokemon + 1
        else:
            print "You have input an incorrect reigon. Please try again."
    elif whatfeature == "Intervals":
        print "Please input the numerical range of pokemon that you would like to view."
        firstnumber = input("What pokedex number would you like to start at? ")
        lastnumber = input("What pokedex number would you like to end at? ")
        print "Here are all of the pokemon in the from "+str(firstnumber)+" to "+str(lastnumber)+":"
        print pokemonlist[firstnumber-1:lastnumber]

    wannacontinue = input("Would you like keep using Dexter? (True or False)")
    print ""
    if wannacontinue == True:
        return pokedex()
    else:
        print "Thank you for using Dexter. Goodbye."
        exit

def pokemonnames(pokemon):
    if pokemon == 1:
        return "Bulbasaur"
    elif pokemon == 2:
        return "Ivysaur"
    elif pokemon == 3:
        return "Venasaur"
    elif pokemon == 4:
        return "Charmander"
    elif pokemon == 5:
        return "Charmeleon"
    elif pokemon == 6:
        return "Charizard"
    elif pokemon == 7:
        return "Squirtle"
    elif pokemon == 8:
        return "Wartortle"
    elif pokemon == 9:
        return "Blastoise"
    elif pokemon == 10:
        return "Caterpie"
    elif pokemon == 11:
        return "Metapod"
    elif pokemon == 12:
        return "Butterfree"
    elif pokemon == 13:
        return "Weedle"
    elif pokemon == 14:
        return "Kakuna"
    elif pokemon == 15:
        return "Beedrill"
    elif pokemon == 16:
        return "Pidgey"
    elif pokemon == 17:
        return "Pidgeotto"
    elif pokemon == 18:
        return "Pidgeot"
    elif pokemon == 19:
        return "Rattata"
    elif pokemon == 20:
        return "Raticate"
    elif pokemon == 21:
        return "Spearow"
    elif pokemon == 22:
        return "Fearow"
    elif pokemon == 23:
        return "Ekans"
    elif pokemon == 24:
        return "Arbok"
    elif pokemon == 25:
        return "Pikachu"
    elif pokemon == 26:
        return "Raichu"
    elif pokemon == 27:
        return "Sandshrew"
    elif pokemon == 28:
        return "Sandslash"
    elif pokemon == 29:
        return "Nidoran(F)"
    elif pokemon == 30:
        return "Nidorina"
    elif pokemon == 31:
        return "Nidoqueen"
    elif pokemon == 32:
        return "Nidoran(M)"
    elif pokemon == 33:
        return "Nidorino"
    elif pokemon == 34:
        return "Nidoking"
    elif pokemon == 35:
        return "Clefairy"
    elif pokemon == 36:
        return "Clefable"
    elif pokemon == 37:
        return "Vulpix"
    elif pokemon == 38:
        return "Ninetails"
    elif pokemon == 39:
        return "Jigglypuff"
    elif pokemon == 40:
        return "Wigglytuff"
    elif pokemon == 41:
        return "Zubat"
    elif pokemon == 42:
        return "Golbat"
    elif pokemon == 43:
        return "Oddish"
    elif pokemon == 44:
        return "Gloom"
    elif pokemon == 45:
        return "Vileplume"
    elif pokemon == 46:
        return "Paras"
    elif pokemon == 47:
        return "Parasect"
    elif pokemon == 48:
        return "Venonat"
    elif pokemon == 49:
        return "Venomoth"
    elif pokemon == 50:
        return "Diglett"
    elif pokemon == 51:
        return "Dugtrio"
    elif pokemon == 52:
        return "Meowth"
    elif pokemon == 53:
        return "Persian"
    elif pokemon == 54:
        return "Psyduck"
    elif pokemon == 55:
        return "Golduck"
    elif pokemon == 56:
        return "Mankey"
    elif pokemon == 57:
        return "Primape"
    elif pokemon == 58:
        return "Growlithe"
    elif pokemon == 59:
        return "Arcanine"
    elif pokemon == 60:
        return "Poliwag"
    elif pokemon == 61:
        return "Poliwhirl"
    elif pokemon == 62:
        return "Poliwrath"
    elif pokemon == 63:
        return "Abra"
    elif pokemon == 64:
        return "Kadabra"
    elif pokemon == 65:
        return "Alakazam"
    elif pokemon == 66:
        return "Machop"
    elif pokemon == 67:
        return "Machoke"
    elif pokemon == 68:
        return "Machamp"
    elif pokemon == 69:
        return "Bellsprout"
    elif pokemon == 70:
        return "Weepinbell"
    elif pokemon == 71:
        return "Victreebel"
    elif pokemon == 72:
        return "Tentacool"
    elif pokemon == 73:
        return "Tentacruel"
    elif pokemon == 74:
        return "Geodude"
    elif pokemon == 75:
        return "Graveler"
    elif pokemon == 76:
        return "Golem"
    elif pokemon == 77:
        return "Ponyta"
    elif pokemon == 78:
        return "Rapidash"
    elif pokemon == 79:
        return "Slowpoke"
    elif pokemon == 80:
        return "Slowbro"
    elif pokemon == 81:
        return "Magnemite"
    elif pokemon == 82:
        return "Magneton"
    elif pokemon == 83:
        return "Farfetch'd"
    elif pokemon == 84:
        return "Doduo"
    elif pokemon == 85:
        return "Dodrio"
    elif pokemon == 86:
        return "Seel"
    elif pokemon == 87:
        return "Dewgong"
    elif pokemon == 88:
        return "Grimer"
    elif pokemon == 89:
        return "Muk"
    elif pokemon == 90:
        return "Shellder"
    elif pokemon == 91:
        return "Cloyster"
    elif pokemon == 92:
        return "Gastly"
    elif pokemon == 93:
        return "Haunter"
    elif pokemon == 94:
        return "Gengar"
    elif pokemon == 95:
        return "Onix"
    elif pokemon == 96:
        return "Drowzee"
    elif pokemon == 97:
        return "Hypno"
    elif pokemon == 98:
        return "Krabby"
    elif pokemon == 99:
        return "Kingler"
    elif pokemon == 100:
        return "Voltorb"
    elif pokemon == 101:
        return "Electrode"
    elif pokemon == 102:
        return "Exeggcute"
    elif pokemon == 103:
        return "Exeggutor"
    elif pokemon == 104:
        return "Cubone"
    elif pokemon == 105:
        return "Marowak"
    elif pokemon == 106:
        return "Hitmonlee"
    elif pokemon == 107:
        return "Hitmonchan"
    elif pokemon == 108:
        return "Lickitung"
    elif pokemon == 109:
        return "Koffing"
    elif pokemon == 110:
        return "Weezing"
    elif pokemon == 111:
        return "Rhyhorn"
    elif pokemon == 112:
        return "Rhydon"
    elif pokemon == 113:
        return "Chansey"
    elif pokemon == 114:
        return "Tangela"
    elif pokemon == 115:
        return "Kangaskhan"
    elif pokemon == 116:
        return "Horsea"
    elif pokemon == 117:
        return "Seadra"
    elif pokemon == 118:
        return "Goldeen"
    elif pokemon == 119:
        return "Seaking"
    elif pokemon == 120:
        return "Staryu"
    elif pokemon == 121:
        return "Starmie"
    elif pokemon == 122:
        return "Mr. Mime"
    elif pokemon == 123:
        return "Scyther"
    elif pokemon == 124:
        return "Jynx"
    elif pokemon == 125:
        return "Electabuzz"
    elif pokemon == 126:
        return "Magmar"
    elif pokemon == 127:
        return "Pinsir"
    elif pokemon == 128:
        return "Tauros"
    elif pokemon == 129:
        return "Magikarp"
    elif pokemon == 130:
        return "Gyarados"
    elif pokemon == 131:
        return "Lapras"
    elif pokemon == 132:
        return "Ditto"
    elif pokemon == 133:
        return "Eevee"
    elif pokemon == 134:
        return "Vaporeon"
    elif pokemon == 135:
        return "Jolteon"
    elif pokemon == 136:
        return "Flareon"
    elif pokemon == 137:
        return "Porygon"
    elif pokemon == 138:
        return "Omanyte"
    elif pokemon == 139:
        return "Omastar"
    elif pokemon == 140:
        return "Kabuto"
    elif pokemon == 141:
        return "Kabutops"
    elif pokemon == 142:
        return "Aerodactyl"
    elif pokemon == 143:
        return "Snorlax"
    elif pokemon == 144:
        return "Articuno"
    elif pokemon == 145:
        return "Zapdos"
    elif pokemon == 146:
        return "Moltres"
    elif pokemon == 147:
        return "Dratini"
    elif pokemon == 148:
        return "Dragonair"
    elif pokemon == 149:
        return "Dragonite"
    elif pokemon == 150:
        return "Mewtwo"
    elif pokemon == 151:
        return "Mew"
    elif pokemon == 152:
        return "Chikorita"
    elif pokemon == 153:
        return "Bayleef"
    elif pokemon == 154:
        return "Meganium"
    elif pokemon == 155:
        return "Cyndaquil"
    elif pokemon == 156:
        return "Quilava"
    elif pokemon == 157:
        return "Typhlosion"
    elif pokemon == 158:
        return "Totodile"
    elif pokemon == 159:
        return "Croconaw"
    elif pokemon == 160:
        return "Feraligatr"
    elif pokemon == 161:
        return "Sentret"
    elif pokemon == 162:
        return "Furret"
    elif pokemon == 163:
        return "Hoothoot"
    elif pokemon == 164:
        return "Noctowl"
    elif pokemon == 165:
        return "Ledyba"
    elif pokemon == 166:
        return "Ledian"
    elif pokemon == 167:
        return "Spinarak"
    elif pokemon == 168:
        return "Ariados"
    elif pokemon == 169:
        return "Crobat"
    elif pokemon == 170:
        return "Chinchou"
    elif pokemon == 171:
        return "Lanturn"
    elif pokemon == 172:
        return "Pichu"
    elif pokemon == 173:
        return "Cleffa"
    elif pokemon == 174:
        return "Igglybuff"
    elif pokemon == 175:
        return "Togepi"
    elif pokemon == 176:
        return "Togetic"
    elif pokemon == 177:
        return "Natu"
    elif pokemon == 178:
        return "Xatu"
    elif pokemon == 179:
        return "Mareep"
    elif pokemon == 180:
        return "Flaaffy"
    elif pokemon == 181:
        return "Ampharos"
    elif pokemon == 182:
        return "Bellossom"
    elif pokemon == 183:
        return "Marill"
    elif pokemon == 184:
        return "Azumarill"
    elif pokemon == 185:
        return "Sudowoodo"
    elif pokemon == 186:
        return "Politoed"
    elif pokemon == 187:
        return "Hoppip"
    elif pokemon == 188:
        return "Skiploom"
    elif pokemon == 189:
        return "Jumpluff"
    elif pokemon == 190:
        return "Aipom"
    elif pokemon == 191:
        return "Sunkern"
    elif pokemon == 192:
        return "Sunflora"
    elif pokemon == 193:
        return "Yanma"
    elif pokemon == 194:
        return "Wooper"
    elif pokemon == 195:
        return "Quagsire"
    elif pokemon == 196:
        return "Espeon"
    elif pokemon == 197:
        return "Umbreon"
    elif pokemon == 198:
        return "Murkrow"
    elif pokemon == 199:
        return "Slowking"
    elif pokemon == 200:
        return "Misdreavus"
    elif pokemon == 201:
        return "Unown"
    elif pokemon == 202:
        return "Wobbuffet"
    elif pokemon == 203:
        return "Girafarig"
    elif pokemon == 204:
        return "Pineco"
    elif pokemon == 205:
        return "Forretress"
    elif pokemon == 206:
        return "Dunsparce"
    elif pokemon == 207:
        return "Gligar"
    elif pokemon == 208:
        return "Steelix"
    elif pokemon == 209:
        return "Snubbull"
    elif pokemon == 210:
        return "Granbull"
    elif pokemon == 211:
        return "Quilfish"
    elif pokemon == 212:
        return "Scizor"
    elif pokemon == 213:
        return "Shuckle"
    elif pokemon == 214:
        return "Heracross"
    elif pokemon == 215:
        return "Sneasel"
    elif pokemon == 216:
        return "Teddiursa"
    elif pokemon == 217:
        return "Ursaring"
    elif pokemon == 218:
        return "Slugma"
    elif pokemon == 219:
        return "Magcargo"
    elif pokemon == 220:
        return "Swinub"
    elif pokemon == 221:
        return "Piloswine"
    elif pokemon == 222:
        return "Corsola"
    elif pokemon == 223:
        return "Remoraid"
    elif pokemon == 224:
        return "Octillery"
    elif pokemon == 225:
        return "Delibird"
    elif pokemon == 226:
        return "Mantine"
    elif pokemon == 227:
        return "Skarmory"
    elif pokemon == 228:
        return "Houndour"
    elif pokemon == 229:
        return "Houndoom"
    elif pokemon == 230:
        return "Kingdra"
    elif pokemon == 231:
        return "Phanpy"
    elif pokemon == 232:
        return "Donphan"
    elif pokemon == 233:
        return "Porygon2"
    elif pokemon == 234:
        return "Stantler"
    elif pokemon == 235:
        return "Smeargle"
    elif pokemon == 236:
        return "Tyrogue"
    elif pokemon == 237:
        return "Hitmontop"
    elif pokemon == 238:
        return "Smoochum"
    elif pokemon == 239:
        return "Elekid"
    elif pokemon == 240:
        return "Magby"
    elif pokemon == 241:
        return "Miltank"
    elif pokemon == 242:
        return "Blissey"
    elif pokemon == 243:
        return "Raikou"
    elif pokemon == 244:
        return "Entei"
    elif pokemon == 245:
        return "Suicune"
    elif pokemon == 246:
        return "Larvitar"
    elif pokemon == 247:
        return "Pupitar"
    elif pokemon == 248:
        return "Tyranitar"
    elif pokemon == 249:
        return "Lugia"
    elif pokemon == 250:
        return "Ho-Oh"
    elif pokemon == 251:
        return "Celebi"
    elif pokemon == 252:
        return "Treecko"
    elif pokemon == 253:
        return "Grovyle"
    elif pokemon == 254:
        return "Sceptile"
    elif pokemon == 255:
        return "Torchic"
    elif pokemon == 256:
        return "Combusken"
    elif pokemon == 257:
        return "Blaziken"
    elif pokemon == 258:
        return "Mudkip"
    elif pokemon == 259:
        return "Marshtomp"
    elif pokemon == 260:
        return "Swampert"
    elif pokemon == 261:
        return "Poochyena"
    elif pokemon == 262:
        return "Mightyena"
    elif pokemon == 263:
        return "Zigzagoon"
    elif pokemon == 264:
        return "Linoone"
    elif pokemon == 265:
        return "Wurmple"
    elif pokemon == 266:
        return "Silcoon"
    elif pokemon == 267:
        return "Beautifly"
    elif pokemon == 268:
        return "Cascoon"
    elif pokemon == 269:
        return "Dustox"
    elif pokemon == 270:
        return "Lotad"
    elif pokemon == 271:
        return "Lombre"
    elif pokemon == 272:
        return "Ludicolo"
    elif pokemon == 273:
        return "Seedot"
    elif pokemon == 274:
        return "Nuzleaf"
    elif pokemon == 275:
        return "Shiftry"
    elif pokemon == 276:
        return "Taillow"
    elif pokemon == 277:
        return "Swellow"
    elif pokemon == 278:
        return "Wingull"
    elif pokemon == 279:
        return "Pelipper"
    elif pokemon == 280:
        return "Ralts"
    elif pokemon == 281:
        return "Kirlia"
    elif pokemon == 282:
        return "Gardevoir"
    elif pokemon == 283:
        return "Surskit"
    elif pokemon == 284:
        return "Masquerain"
    elif pokemon == 285:
        return "Shroomish"
    elif pokemon == 286:
        return "Breloom"
    elif pokemon == 287:
        return "Slakoth"
    elif pokemon == 288:
        return "Vigoroth"
    elif pokemon == 289:
        return "Slaking"
    elif pokemon == 290:
        return "Nincada"
    elif pokemon == 291:
        return "Ninjask"
    elif pokemon == 292:
        return "Shedinja"
    elif pokemon == 293:
        return "Whismur"
    elif pokemon == 294:
        return "Loudred"
    elif pokemon == 295:
        return "Exploud"
    elif pokemon == 296:
        return "Makuhita"
    elif pokemon == 297:
        return "Hariyama"
    elif pokemon == 298:
        return "Azurill"
    elif pokemon == 299:
        return "Nosepass"
    elif pokemon == 300:
        return "Skitty"
    elif pokemon == 301:
        return "Delcatty"
    elif pokemon == 302:
        return "Sableye"
    elif pokemon == 303:
        return "Mawile"
    elif pokemon == 304:
        return "Aron"
    elif pokemon == 305:
        return "Lairon"
    elif pokemon == 306:
        return "Aggron"
    elif pokemon == 307:
        return "Meditite"
    elif pokemon == 308:
        return "Medicham"
    elif pokemon == 309:
        return "Electrike"
    elif pokemon == 310:
        return "Manectric"
    elif pokemon == 311:
        return "Plusle"
    elif pokemon == 312:
        return "Minun"
    elif pokemon == 313:
        return "Volbeat"
    elif pokemon == 314:
        return "Illumise"
    elif pokemon == 315:
        return "Roselia"
    elif pokemon == 316:
        return "Gulpin"
    elif pokemon == 317:
        return "Swalot"
    elif pokemon == 318:
        return "Carvanha"
    elif pokemon == 319:
        return "Sharpedo"
    elif pokemon == 320:
        return "Wailmer"
    elif pokemon == 321:
        return "Wailord"
    elif pokemon == 322:
        return "Numel"
    elif pokemon == 323:
        return "Camerupt"
    elif pokemon == 324:
        return "Torkoal"
    elif pokemon == 325:
        return "Spoink"
    elif pokemon == 326:
        return "Grumpig"
    elif pokemon == 327:
        return "Spinda"
    elif pokemon == 328:
        return "Trapinch"
    elif pokemon == 329:
        return "Vibrava"
    elif pokemon == 330:
        return "Flygon"
    elif pokemon == 331:
        return "Cacnea"
    elif pokemon == 332:
        return "Cacturne"
    elif pokemon == 333:
        return "Swablu"
    elif pokemon == 334:
        return "Altaria"
    elif pokemon == 335:
        return "Zangoose"
    elif pokemon == 336:
        return "Seviper"
    elif pokemon == 337:
        return "Lunatone"
    elif pokemon == 338:
        return "Solrock"
    elif pokemon == 339:
        return "Barboach"
    elif pokemon == 340:
        return "Whiscash"
    elif pokemon == 341:
        return "Corphish"
    elif pokemon == 342:
        return "Crawdaunt"
    elif pokemon == 343:
        return "Baltoy"
    elif pokemon == 344:
        return "Claydol"
    elif pokemon == 345:
        return "Lileep"
    elif pokemon == 346:
        return "Cradily"
    elif pokemon == 347:
        return "Anorith"
    elif pokemon == 348:
        return "Armaldo"
    elif pokemon == 349:
        return "Feebas"
    elif pokemon == 350:
        return "Milotic"
    elif pokemon == 351:
        return "Castform"
    elif pokemon == 352:
        return "Kecleon"
    elif pokemon == 353:
        return "Shuppet"
    elif pokemon == 354:
        return "Banette"
    elif pokemon == 355:
        return "Duskull"
    elif pokemon == 356:
        return "Dusclops"
    elif pokemon == 357:
        return "Tropius"
    elif pokemon == 358:
        return "Chimecho"
    elif pokemon == 359:
        return "Absol"
    elif pokemon == 360:
        return "Wynaut"
    elif pokemon == 361:
        return "Snorunt"
    elif pokemon == 362:
        return "Glalie"
    elif pokemon == 363:
        return "Spheal"
    elif pokemon == 364:
        return "Sealeo"
    elif pokemon == 365:
        return "Walrein"
    elif pokemon == 366:
        return "Clamperl"
    elif pokemon == 367:
        return "Huntail"
    elif pokemon == 368:
        return "Gorebyss"
    elif pokemon == 369:
        return "Relicanth"
    elif pokemon == 370:
        return "Luvdisc"
    elif pokemon == 371:
        return "Bagon"
    elif pokemon == 372:
        return "Shelgon"
    elif pokemon == 373:
        return "Salamence"
    elif pokemon == 374:
        return "Beldum"
    elif pokemon == 375:
        return "Metang"
    elif pokemon == 376:
        return "Metagross"
    elif pokemon == 377:
        return "Regirock"
    elif pokemon == 378:
        return "Regice"
    elif pokemon == 379:
        return "Registeel"
    elif pokemon == 380:
        return "Latias"
    elif pokemon == 381:
        return "Latios"
    elif pokemon == 382:
        return "Kyogre"
    elif pokemon == 383:
        return "Groudon"
    elif pokemon == 384:
        return "Rayquaza"
    elif pokemon == 385:
        return "Jirachi"
    elif pokemon == 386:
        return "Deoxys"
    elif pokemon == 387:
        return "Turtwig"
    elif pokemon == 388:
        return "Grotle"
    elif pokemon == 389:
        return "Torterra"
    elif pokemon == 390:
        return "Chimchar"
    elif pokemon == 391:
        return "Monferno"
    elif pokemon == 392:
        return "Infernape"
    elif pokemon == 393:
        return "Piplup"
    elif pokemon == 394:
        return "Primplup"
    elif pokemon == 395:
        return "Empoleon"
    elif pokemon == 396:
        return "Starly"
    elif pokemon == 397:
        return "Staravia"
    elif pokemon == 398:
        return "Staraptor"
    elif pokemon == 399:
        return "Bidoof"
    elif pokemon == 400:
        return "Bibarel"
    elif pokemon == 401:
        return "Kricketot"
    elif pokemon == 402:
        return "Kricketune"
    elif pokemon == 403:
        return "Shinx"
    elif pokemon == 404:
        return "Luxio"
    elif pokemon == 405:
        return "Luxray"
    elif pokemon == 406:
        return "Budew"
    elif pokemon == 407:
        return "Roserade"
    elif pokemon == 408:
        return "Cranidos"
    elif pokemon == 409:
        return "Rampardos"
    elif pokemon == 410:
        return "Shieldon"
    elif pokemon == 411:
        return "Bastiodon"
    elif pokemon == 412:
        return "Burmy"
    elif pokemon == 413:
        return "Wormadam"
    elif pokemon == 414:
        return "Mothim"
    elif pokemon == 415:
        return "Combee"
    elif pokemon == 416:
        return "Vespiquen"
    elif pokemon == 417:
        return "Pachirisu"
    elif pokemon == 418:
        return "Buizel"
    elif pokemon == 419:
        return "Floatzel"
    elif pokemon == 420:
        return "Cherubi"
    elif pokemon == 421:
        return "Cherrim"
    elif pokemon == 422:
        return "Shellos"
    elif pokemon == 423:
        return "Gastrodon"
    elif pokemon == 424:
        return "Ambipom"
    elif pokemon == 425:
        return "Drifloon"
    elif pokemon == 426:
        return "Drifblim"
    elif pokemon == 427:
        return "Buneary"
    elif pokemon == 428:
        return "Lopunny"
    elif pokemon == 429:
        return "Mismagius"
    elif pokemon == 430:
        return "Honchkrow"
    elif pokemon == 431:
        return "Glameow"
    elif pokemon == 432:
        return "Purugly"
    elif pokemon == 433:
        return "Chingling"
    elif pokemon == 434:
        return "Stunky"
    elif pokemon == 435:
        return "Skuntank"
    elif pokemon == 436:
        return "Bronzor"
    elif pokemon == 437:
        return "Bronzong"
    elif pokemon == 438:
        return "Bonsly"
    elif pokemon == 439:
        return "Mime Jr."
    elif pokemon == 440:
        return "Happiny"
    elif pokemon == 441:
        return "Chatot"
    elif pokemon == 442:
        return "Spiritomb"
    elif pokemon == 443:
        return "Gible"
    elif pokemon == 444:
        return "Gabite"
    elif pokemon == 445:
        return "Garchomp"
    elif pokemon == 446:
        return "Munchlax"
    elif pokemon == 447:
        return "Riolu"
    elif pokemon == 448:
        return "Lucario"
    elif pokemon == 449:
        return "Hippopotas"
    elif pokemon == 450:
        return "Hippowdon"
    elif pokemon == 451:
        return "Skorupi"
    elif pokemon == 452:
        return "Drapion"
    elif pokemon == 453:
        return "Croagunk"
    elif pokemon == 454:
        return "Toxicroak"
    elif pokemon == 455:
        return "Carnivine"
    elif pokemon == 456:
        return "Finneon"
    elif pokemon == 457:
        return "Lumineon"
    elif pokemon == 458:
        return "Mantyke"
    elif pokemon == 459:
        return "Snover"
    elif pokemon == 460:
        return "Abomasnow"
    elif pokemon == 461:
        return "Weavile"
    elif pokemon == 462:
        return "Magnezone"
    elif pokemon == 463:
        return "Lickilicky"
    elif pokemon == 464:
        return "Rhyperior"
    elif pokemon == 465:
        return "Tangrowth"
    elif pokemon == 466:
        return "Electivire"
    elif pokemon == 467:
        return "Magmortar"
    elif pokemon == 468:
        return "Togekiss"
    elif pokemon == 469:
        return "Yanmega"
    elif pokemon == 470:
        return "Leafeon"
    elif pokemon == 471:
        return "Glaceon"
    elif pokemon == 472:
        return "Gliscor"
    elif pokemon == 473:
        return "Mamoswine"
    elif pokemon == 474:
        return "Porygon-Z"
    elif pokemon == 475:
        return "Gallade"
    elif pokemon == 476:
        return "Probopass"
    elif pokemon == 477:
        return "Dusknoir"
    elif pokemon == 478:
        return "Froslass"
    elif pokemon == 479:
        return "Rotom"
    elif pokemon == 480:
        return "Uxie"
    elif pokemon == 481:
        return "Mesprit"
    elif pokemon == 482:
        return "Azelf"
    elif pokemon == 483:
        return "Dialga"
    elif pokemon == 484:
        return "Palkia"
    elif pokemon == 485:
        return "Heatran"
    elif pokemon == 486:
        return "Regigigas"
    elif pokemon == 487:
        return "Giratina"
    elif pokemon == 488:
        return "Cresselia"
    elif pokemon == 489:
        return "Phione"
    elif pokemon == 490:
        return "Manaphy"
    elif pokemon == 491:
        return "Darkrai"
    elif pokemon == 492:
        return "Shaymin"
    elif pokemon == 493:
        return "Arceus"
    elif pokemon == 494:
        return "Victini"
    elif pokemon == 495:
        return "Snivy"
    elif pokemon == 496:
        return "Servine"
    elif pokemon == 497:
        return "Serperior"
    elif pokemon == 498:
        return "Tepig"
    elif pokemon == 499:
        return "Pignite"
    elif pokemon == 500:
        return "Emboar"
    elif pokemon == 501:
        return "Oshawott"
    elif pokemon == 502:
        return "Dewott"
    elif pokemon == 503:
        return "Samurott"
    elif pokemon == 504:
        return "Patrat"
    elif pokemon == 505:
        return "Watchog"
    elif pokemon == 506:
        return "Lillipup"
    elif pokemon == 507:
        return "Herdier"
    elif pokemon == 508:
        return "Stoutland"
    elif pokemon == 509:
        return "Purrloin"
    elif pokemon == 510:
        return "Liepard"
    elif pokemon == 511:
        return "Pansage"
    elif pokemon == 512:
        return "Simisage"
    elif pokemon == 513:
        return "Pansear"
    elif pokemon == 514:
        return "Simisear"
    elif pokemon == 515:
        return "Panpour"
    elif pokemon == 516:
        return "Simipour"
    elif pokemon == 517:
        return "Munna"
    elif pokemon == 518:
        return "Musharna"
    elif pokemon == 519:
        return "Pidove"
    elif pokemon == 520:
        return "Tranquill"
    elif pokemon == 521:
        return "Unfezant"
    elif pokemon == 522:
        return "Blitzle"
    elif pokemon == 523:
        return "Zebstrika"
    elif pokemon == 524:
        return "Roggenrola"
    elif pokemon == 525:
        return "Boldore"
    elif pokemon == 526:
        return "Gigalith"
    elif pokemon == 527:
        return "Woobat"
    elif pokemon == 528:
        return "Swoobat"
    elif pokemon == 529:
        return "Drilbur"
    elif pokemon == 530:
        return "Excadrill"
    elif pokemon == 531:
        return "Audino"
    elif pokemon == 532:
        return "Timburr"
    elif pokemon == 533:
        return "Gurdurr"
    elif pokemon == 534:
        return "Conkeldurr"
    elif pokemon == 535:
        return "Tympole"
    elif pokemon == 536:
        return "Palpitoad"
    elif pokemon == 537:
        return "Seismitoad"
    elif pokemon == 538:
        return "Throh"
    elif pokemon == 539:
        return "Sawk"
    elif pokemon == 540:
        return "Sewaddle"
    elif pokemon == 541:
        return "Swadloon"
    elif pokemon == 542:
        return "Leavanny"
    elif pokemon == 543:
        return "Venipede"
    elif pokemon == 544:
        return "Whirlipede"
    elif pokemon == 545:
        return "Scolipede"
    elif pokemon == 546:
        return "Cottonee"
    elif pokemon == 547:
        return "Whimsicott"
    elif pokemon == 548:
        return "Petilil"
    elif pokemon == 549:
        return "Lilligant"
    elif pokemon == 550:
        return "Basculin"
    elif pokemon == 551:
        return "Sandile"
    elif pokemon == 552:
        return "Krokorok"
    elif pokemon == 553:
        return "Krookodile"
    elif pokemon == 554:
        return "Darumaka"
    elif pokemon == 555:
        return "Darmanitan"
    elif pokemon == 556:
        return "Maractus"
    elif pokemon == 557:
        return "Dwebble"
    elif pokemon == 558:
        return "Crustle"
    elif pokemon == 559:
        return "Scraggy"
    elif pokemon == 560:
        return "Scrafty"
    elif pokemon == 561:
        return "Sigilyph"
    elif pokemon == 562:
        return "Yamask"
    elif pokemon == 563:
        return "Cofagrigus"
    elif pokemon == 564:
        return "Tirtouga"
    elif pokemon == 565:
        return "Carracosta"
    elif pokemon == 566:
        return "Archen"
    elif pokemon == 567:
        return "Archeops"
    elif pokemon == 568:
        return "Trubbish"
    elif pokemon == 569:
        return "Garbodor"
    elif pokemon == 570:
        return "Zorua"
    elif pokemon == 571:
        return "Zoroark"
    elif pokemon == 572:
        return "Minccino"
    elif pokemon == 573:
        return "Cinccino"
    elif pokemon == 574:
        return "Gothita"
    elif pokemon == 575:
        return "Gothorita"
    elif pokemon == 576:
        return "Gothitelle"
    elif pokemon == 577:
        return "Solosis"
    elif pokemon == 578:
        return "Duosion"
    elif pokemon == 579:
        return "Reuniclus"
    elif pokemon == 580:
        return "Ducklett"
    elif pokemon == 581:
        return "Swanna"
    elif pokemon == 582:
        return "Valillite"
    elif pokemon == 583:
        return "Vanillish"
    elif pokemon == 584:
        return "Vanilluxe"
    elif pokemon == 585:
        return "Deerling"
    elif pokemon == 586:
        return "Sawsbuck"
    elif pokemon == 587:
        return "Emolga"
    elif pokemon == 588:
        return "Karrablast"
    elif pokemon == 589:
        return "Escavalier"
    elif pokemon == 590:
        return "Foongus"
    elif pokemon == 591:
        return "Amoonguss"
    elif pokemon == 592:
        return "Frillish"
    elif pokemon == 593:
        return "Jellicent"
    elif pokemon == 594:
        return "Alomomola"
    elif pokemon == 595:
        return "Joltik"
    elif pokemon == 596:
        return "Galvantula"
    elif pokemon == 597:
        return "Ferroseed"
    elif pokemon == 598:
        return "Ferrothorn"
    elif pokemon == 599:
        return "Klink"
    elif pokemon == 600:
        return "Klang"
    elif pokemon == 601:
        return "Klinklang"
    elif pokemon == 602:
        return "Tynamo"
    elif pokemon == 603:
        return "Eelektrik"
    elif pokemon == 604:
        return "Eelektross"
    elif pokemon == 605:
        return "Elgyem"
    elif pokemon == 606:
        return "Beheeyem"
    elif pokemon == 607:
        return "Litwick"
    elif pokemon == 608:
        return "Lampent"
    elif pokemon == 609:
        return "Chandelure"
    elif pokemon == 610:
        return "Axew"
    elif pokemon == 611:
        return "Fraxure"
    elif pokemon == 612:
        return "Haxorus"
    elif pokemon == 613:
        return "Cubchoo"
    elif pokemon == 614:
        return "Beartic"
    elif pokemon == 615:
        return "Cryogonal"
    elif pokemon == 616:
        return "Shelmet"
    elif pokemon == 617:
        return "Accelgor"
    elif pokemon == 618:
        return "Stunfisk"
    elif pokemon == 619:
        return "Mienfoo"
    elif pokemon == 620:
        return "Mienshao"
    elif pokemon == 621:
        return "Druddigon"
    elif pokemon == 622:
        return "Golett"
    elif pokemon == 623:
        return "Golurk"
    elif pokemon == 624:
        return "Pawniard"
    elif pokemon == 625:
        return "Bisharp"
    elif pokemon == 626:
        return "Bouffalant"
    elif pokemon == 627:
        return "Rufflet"
    elif pokemon == 628:
        return "Braviary"
    elif pokemon == 629:
        return "Vullaby"
    elif pokemon == 630:
        return "Mandibuzz"
    elif pokemon == 631:
        return "Heatmor"
    elif pokemon == 632:
        return "Durant"
    elif pokemon == 633:
        return "Deino"
    elif pokemon == 634:
        return "Zweilous"
    elif pokemon == 635:
        return "Hydreigon"
    elif pokemon == 636:
        return "Larvesta"
    elif pokemon == 637:
        return "Volcarona"
    elif pokemon == 638:
        return "Cobalion"
    elif pokemon == 639:
        return "Terrakion"
    elif pokemon == 640:
        return "Virizion"
    elif pokemon == 641:
        return "Tornadus"
    elif pokemon == 642:
        return "Thundurus"
    elif pokemon == 643:
        return "Reshiram"
    elif pokemon == 644:
        return "Zekrom"
    elif pokemon == 645:
        return "Landorus"
    elif pokemon == 646:
        return "Kyurem"
    elif pokemon == 647:
        return "Keldeo"
    elif pokemon == 648:
        return "Meloetta"
    elif pokemon == 649:
        return "Genesect"
    elif pokemon == 650:
        return "Chespin"
    elif pokemon == 651:
        return "Quilladin"
    elif pokemon == 652:
        return "Chesnaught"
    elif pokemon == 653:
        return "Fennekin"
    elif pokemon == 654:
        return "Braixen"
    elif pokemon == 655:
        return "Delphox"
    elif pokemon == 656:
        return "Froakie"
    elif pokemon == 657:
        return "Frogadier"
    elif pokemon == 658:
        return "Greninja"
    elif pokemon == 659:
        return "Bunnelby"
    elif pokemon == 660:
        return "Diggersby"
    elif pokemon == 661:
        return "Fletchling"
    elif pokemon == 662:
        return "Fletchinder"
    elif pokemon == 663:
        return "Talonflame"
    elif pokemon == 664:
        return "Scatterbug"
    elif pokemon == 665:
        return "Spewpa"
    elif pokemon == 666:
        return "Vivillon"
    elif pokemon == 667:
        return "Litleo"
    elif pokemon == 668:
        return "Pyroar"
    elif pokemon == 669:
        return "Flabébé"
    elif pokemon == 670:
        return "Floette"
    elif pokemon == 671:
        return "Florges"
    elif pokemon == 672:
        return "Skiddo"
    elif pokemon == 673:
        return "Gogoat"
    elif pokemon == 674:
        return "Pancham"
    elif pokemon == 675:
        return "Pangoro"
    elif pokemon == 676:
        return "Furfrou"
    elif pokemon == 677:
        return "Espurr"
    elif pokemon == 678:
        return "Meowstic"
    elif pokemon == 679:
        return "Honedge"
    elif pokemon == 680:
        return "Doublade"
    elif pokemon == 681:
        return "Aegislash"
    elif pokemon == 682:
        return "Spritzee"
    elif pokemon == 683:
        return "Aromatisse"
    elif pokemon == 684:
        return "Swirlix"
    elif pokemon == 685:
        return "Slurpuff"
    elif pokemon == 686:
        return "Inkay"
    elif pokemon == 687:
        return "Malamar"
    elif pokemon == 688:
        return "Binacle"
    elif pokemon == 689:
        return "Barbaracle"
    elif pokemon == 690:
        return "Skrelp"
    elif pokemon == 691:
        return "Dragalge"
    elif pokemon == 692:
        return "Clauncher"
    elif pokemon == 693:
        return "Clawitzer"
    elif pokemon == 694:
        return "Helioptile"
    elif pokemon == 695:
        return "Heliolisk"
    elif pokemon == 696:
        return "Tyrunt"
    elif pokemon == 697:
        return "Tyrantrum"
    elif pokemon == 698:
        return "Amaura"
    elif pokemon == 699:
        return "Aurorus"
    elif pokemon == 700:
        return "Sylveon"
    elif pokemon == 701:
        return "Hawlucha"
    elif pokemon == 702:
        return "Dedenne"
    elif pokemon == 703:
        return "Carbink"
    elif pokemon == 704:
        return "Goomy"
    elif pokemon == 705:
        return "Sliggoo"
    elif pokemon == 706:
        return "Goodra"
    elif pokemon == 707:
        return "Klefki"
    elif pokemon == 708:
        return "Phantump"
    elif pokemon == 709:
        return "Trevenant"
    elif pokemon == 710:
        return "Pumpkaboo"
    elif pokemon == 711:
        return "Gourgeist"
    elif pokemon == 712:
        return "Bergmite"
    elif pokemon == 713:
        return "Avalugg"
    elif pokemon == 714:
        return "Noibat"
    elif pokemon == 715:
        return "Noivern"
    elif pokemon == 716:
        return "Xerneas"
    elif pokemon == 717:
        return "Yveltal"
    elif pokemon == 718:
        return "Zygarde"
    elif pokemon == 719:
        return "Diancie"
    elif pokemon == 720:
        return "Hoopa"
    elif pokemon == 721:
        return "Volcanion"
    else:
        return "You have entered an incorrect number. Please enter a number from 1 to 721."
