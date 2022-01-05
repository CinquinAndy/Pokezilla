import asyncio
import re

import aiohttp

url = "https://pokeapi.co/api/v2/pokemon"
url2 = "https://pokeapi.co/api/v2/pokemon-species/"


async def get_pokemon(id_pokemon):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}?offset={int(id_pokemon) - 1}&limit={1}") as r:
            data = await r.json()
            for poke in data['results']:
                async with session.get(f"{poke['url']}") as req:
                    new = await req.json()

                m = re.search(r'/([0-9]+)/$', poke['url']).group()
                to_request = f"{url2}{m}"
                async with session.get(to_request) as req2:
                    result2 = await req2.json()

                    for a in result2['flavor_text_entries']:
                        if a['language']['name'] == 'fr':
                            break

                    for b in result2['genera']:
                        if b['language']['name'] == 'fr':
                            break

                    for c in result2['names']:
                        if c['language']['name'] == 'fr':
                            break

                    pokemon = {
                        "name": poke['name'],
                        "name_fr": c,
                        "stats": new['stats'],
                        "types": new['types'],
                        "height": new['height'],
                        "weight": new['weight'],
                        "capture_rate": result2['capture_rate'],
                        "flavor_text": a,
                        "genera": b,
                        "is_baby": result2['is_baby'],
                        "is_legendary": result2['is_legendary'],
                        "is_mythical": result2['is_mythical'],
                    }
    return pokemon


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(get_pokemon())
