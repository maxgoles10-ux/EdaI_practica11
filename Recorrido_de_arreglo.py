def recorrido_arreglo(array, i=0):
    if i == len(array):
        return 
    print(array[i]) 
    recorrido_arreglo(array, i + 1)   
