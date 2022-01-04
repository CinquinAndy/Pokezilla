from Pokezilla.request import get_pokemon_infos


def moyenne(pokemons):
    result = []
    for pokemon in pokemons:
        result += get_pokemon_infos(pokemon)
    print(result)
