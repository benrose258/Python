def PokemonPeoplePlaces(pokemons,people,places):
    if pokemons==[]:
        return "You can't catch pokemon without pokemon!"
    elif people==[]:
        return "You can't catch pokemon without people!"
    elif places==[]:
        return "You can't catch pokemon if you don't have a place of existence!"
    else:
        combo=1
        for pkmn in pokemons:
            for person in people:
                for place in places:
                    print "Combination "+str(combo)+": "+pkmn+", "+person+", "+place
                    combo=combo+1
