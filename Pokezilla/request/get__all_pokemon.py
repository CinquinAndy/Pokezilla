import asyncio
import re
import aiohttp

url = "https://pokeapi.co/api/v2/pokemon"


async def get_all_pokemon():
    i = 0
    data = []
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}?offset={0}&limit={898}") as r:
            print(f"{i} : {r.status}")
            test = await r.json()
            # print(test)
            for poke in test['results']:
                pokemon = {
                    "name": poke['name'],
                    "id": re.search(r'/([0-9]+)/$', poke['url']).group(1),
                }
                data.append(pokemon)
    return data


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_all_pokemon())