def al_reves(cadena, i=0):
    if i == len(cadena):
        return
    al_reves(cadena, i + 1)
    print(cadena[i], end="")
        