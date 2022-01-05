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
    if averageHp != 0:
        averageHp /= len(pokemons)
    if averageAttack != 0:
        averageAttack /= len(pokemons)
    if averageDefense != 0:
        averageDefense /= len(pokemons)
    if averageAttackSpe != 0:
        averageAttackSpe /= len(pokemons)
    if averageDefenseSpe != 0:
        averageDefenseSpe /= len(pokemons)
    if averageSpeed != 0:
        averageSpeed /= len(pokemons)

    result = {
        "averageHp": averageHp,
        "averageAttack": averageAttack,
        "averageDefense": averageDefense,
        "averageAttackSpe": averageAttackSpe,
        "averageDefenseSpe": averageDefenseSpe,
        "averageSpeed": averageSpeed
    }

    print(result)
    print(HttpResponse(result))

    return HttpResponse(json.dumps(result))
