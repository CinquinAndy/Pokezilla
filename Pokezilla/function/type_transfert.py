def get_weakness(type):
    if type == "Normal":
        return [
            "Rock",
            "Steel",
            "Ghost"
        ]
    elif type == "Fighting":
        return [
            "Flying",
            "Poison",
            "Bug",
            "Psychic",
            "Fairy",
            "Ghosht"
        ]
    elif type == "Flying":
        return [
            "Rock",
            "Steel",
            "Electric"
        ]
    elif type == "Poison":
        return [
            "Poison",
            "Ground",
            "Rock",
            "Ghost",
            "Steel"
        ]
    elif type == "Ground":
        return [
            "Bug",
            "Grass",
            "Flying"
        ]
    elif type == "Rock":
        return [
            "Fighting",
            "Ground",
            "Steel"
        ]
    elif type == "Bug":
        return [
            "Fighting",
            "Flying",
            "Poison",
            "Ghost",
            "Steel",
            "Fire",
            "Fairy"
        ]
    elif type == "Ghost":
        return [
            "Normal",
            "Dark"
        ]
    elif type == "Steel":
        return [
            "Steel",
            "Fire",
            "Water",
            "Electric"
        ]
    elif type == "Fire":
        return [
            "Rock",
            "Fire",
            "Water",
            "Dragon"
        ]
    elif type == "Water":
        return [
            "Water",
            "Grass",
            "Dragon"
        ]
    elif type == "Grass":
        return [
            "Flying",
            "Poison",
            "Bug",
            "Steel",
            "Fire",
            "Grass",
            "Dragon"
        ]
    elif type == "Electric":
        return [
            "Grass",
            "Electric",
            "Dragon",
            "Ground",
        ]
    elif type == "Psychic":
        return [
            "Steel",
            "Psychic",
            "Dark"
        ]
    elif type == "Ice":
        return [
            "Steel",
            "Fire",
            "Water",
            "Ice"
        ]
    elif type == "Dragon":
        return [
            "Steel",
            "Fairy"
        ]
    elif type == "Dark":
        return [
            "Fighting",
            "Dark",
            "Fairy"
        ]
    elif type == "Fairy":
        return [
            "Poison",
            "Steel",
            "Fire"
        ]
