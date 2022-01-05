from Pokezilla.request.get_pokemon_infos import get_pokemon


def moyenne(pokemons):
    result = []
    for pokemon in pokemons:
        result += await get_pokemon(pokemon)
    print(result)
