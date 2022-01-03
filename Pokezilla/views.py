from django.shortcuts import render


def index(request):
    # ici
    contextvalue = {"valeur": "valeurTest", "table": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}
    return render(request, 'index.html', contextvalue)


def pokemon(request, number):
    print(number)
    return render(request, 'pokemon.html', {"number": number})
