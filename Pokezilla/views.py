from django.shortcuts import render

from Pokezilla.request.get__all_pokemon import get_all_pokemon
from Pokezilla.request.get_pokemon_infos import get_pokemon


async def index(request):
	# ici
	data = await get_all_pokemon()
	contextvalue = {"values": data}

	return render(request, 'index.html', contextvalue)


async def pokemon(request, number):
	print(number)
	data = await get_pokemon(number)
	return render(request, 'pokemon.html', {"pokemon": data,"number": number})
