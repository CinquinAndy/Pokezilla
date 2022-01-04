from Pokezilla.request.get_pokemon_infos import *


def moyenne(pokemons):
    result = []
    for pokemon in pokemons:
        result += get_pokemon(pokemon)
    print(result)
