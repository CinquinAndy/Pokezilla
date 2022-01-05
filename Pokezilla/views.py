from django.http import HttpResponse
from django.shortcuts import render

from Pokezilla.request.get__all_pokemon import get_all_pokemon, get_names_pokemons
from Pokezilla.request.get_pokemon_infos import get_pokemon


def testcall(request):
    text = request.POST.getlist('text[]')
    # Do whatever with the input variable text
    response = text
    # Send the response

    return HttpResponse(response)


async def index(request):
    data = await get_all_pokemon()
    contextvalue = {"values": data}

    return render(request, 'index.html', contextvalue)


async def pokemon(request, number):
    print(number)
    data = await get_pokemon(number)
    return render(request, 'pokemon.html', {"pokemon": data, "number": number})
