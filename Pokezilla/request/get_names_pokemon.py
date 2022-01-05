import os
from Pokezilla.models.Pokemon import Pokemon

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


def get_names_pokemons():
    all_pokes = Pokemon.objects.all()
    return all_pokes
