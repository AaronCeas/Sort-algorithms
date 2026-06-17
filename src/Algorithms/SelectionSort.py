def selection_sort(lista):
    n = len(lista)
    
    for i in range(n - 1):

        indice_minimo = i

        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


mi_lista = [64, 25, 12, 22, 11]
selection_sort(mi_lista)
print("Lista ordenada:", mi_lista)