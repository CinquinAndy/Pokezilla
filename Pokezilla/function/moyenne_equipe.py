import json

from django.http import HttpResponse

from Pokezilla.request.get_pokemon_infos import *


async def average(request):
    pokemons = request.POST.getlist('pokemons[]')
    calculs = []
    for pokemon in pokemons:
        data = await get_pokemon(pokemon)
        calculs.append(data['stats'])
    averageHp = 0
    averageAttack = 0
    averageDefense = 0
    averageAttackSpe = 0
    averageDefenseSpe = 0
    averageSpeed = 0
    for calcul in calculs:
        for stat in calcul:
            if stat['stat']['name'] == "hp":
                averageHp += stat['base_stat']
            if stat['stat']['name'] == "attack":
                averageAttack += stat['base_stat']
            if stat['stat']['name'] == "defense":
                averageDefense += stat['base_stat']
            if stat['stat']['name'] == "special-attack":
                averageAttackSpe += stat['base_stat']
            if stat['stat']['name'] == "special-defense":
                averageDefenseSpe += stat['base_stat']
            if stat['stat']['name'] == "speed":
                averageSpeed += stat['base_stat']

    averageHp /= len(pokemons)
    averageAttack /= len(pokemons)
    averageDefense /= len(pokemons)
    averageAttackSpe /= len(pokemons)
    averageDefenseSpe /= len(pokemons)
    averageSpeed /= len(pokemons)

    result = {
        "averageHp": averageHp,
        "averageAttack": averageAttack,
        "averageDefense": averageDefense,
        "averageAttackSpe": averageAttackSpe,
        "averageDefenseSpe": averageDefenseSpe,
        "averageSpeed": averageSpeed
    }

    return HttpResponse(json.dumps(result))
