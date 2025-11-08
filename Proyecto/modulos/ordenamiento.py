
import pandas as pd

def quicksort(lista, key):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)//2]
    menores = [x for x in lista if x[key] < pivote[key]]
    iguales = [x for x in lista if x[key] == pivote[key]]
    mayores = [x for x in lista if x[key] > pivote[key]]

    return quicksort(menores, key) + iguales + quicksort(mayores, key)

def mergesort(lista, key):
    if len(lista) <= 1:
        return lista
    mitad = len(lista)//2
    izquierda = mergesort(lista[:mitad], key)
    derecha = mergesort(izquierda, derecha, key)
    return merge(izquierda, derecha, key)

def merge(izquierda, derecha, key):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][key] <= derecha[j][key]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def ordenar_pedidos(path_csv, key="prioridad", metodo="quicksort"):
    df = pd.read_csv(path_csv)
    pedidos = df.to_dict("records")
    if metodo == "quicksort":
        ordenados = quicksort(pedidos, key)
    else:
        ordenados = mergesort(pedidos, key)
    return pd.DataFrame(ordenados)