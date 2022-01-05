import asyncio
import re
import aiohttp

from Pokezilla.request.get_names_pokemon import get_names_pokemons

url = "https://pokeapi.co/api/v2/pokemon"


async def get_all_pokemon():
    allpoke = get_names_pokemons()

    data = []
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}?offset={0}&limit={898}") as r:
            test = await r.json()
            for poke in test['results']:
                pokemon = {
                    "name": allpoke[int(re.search(r'/([0-9]+)/$', poke['url']).group(1)) - 1].name_fr,
                    "id": re.search(r'/([0-9]+)/$', poke['url']).group(1),
                }
                data.append(pokemon)

    return data


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(get_all_pokemon())
