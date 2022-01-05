def get_weakness(type):
    if type == "normal":
        return [
            "rock",
            "steel",
            "ghost"
        ]
    elif type == "fighting":
        return [
            "flying",
            "poison",
            "bug",
            "psychic",
            "fairy",
            "ghosht"
        ]
    elif type == "flying":
        return [
            "rock",
            "steel",
            "electric"
        ]
    elif type == "poison":
        return [
            "poison",
            "ground",
            "rock",
            "ghost",
            "steel"
        ]
    elif type == "ground":
        return [
            "bug",
            "grass",
            "flying"
        ]
    elif type == "rock":
        return [
            "fighting",
            "ground",
            "steel"
        ]
    elif type == "bug":
        return [
            "fighting",
            "flying",
            "poison",
            "ghost",
            "steel",
            "fire",
            "fairy"
        ]
    elif type == "ghost":
        return [
            "normal",
            "dark"
        ]
    elif type == "steel":
        return [
            "steel",
            "fire",
            "water",
            "electric"
        ]
    elif type == "fire":
        return [
            "rock",
            "fire",
            "water",
            "dragon"
        ]
    elif type == "water":
        return [
            "water",
            "grass",
            "dragon"
        ]
    elif type == "grass":
        return [
            "flying",
            "poison",
            "bug",
            "steel",
            "fire",
            "grass",
            "dragon"
        ]
    elif type == "electric":
        return [
            "grass",
            "electric",
            "dragon",
            "ground",
        ]
    elif type == "psychic":
        return [
            "steel",
            "psychic",
            "dark"
        ]
    elif type == "ice":
        return [
            "steel",
            "fire",
            "water",
            "ice"
        ]
    elif type == "dragon":
        return [
            "steel",
            "fairy"
        ]
    elif type == "dark":
        return [
            "fighting",
            "dark",
            "fairy"
        ]
    elif type == "fairy":
        return [
            "poison",
            "steel",
            "fire"
        ]
