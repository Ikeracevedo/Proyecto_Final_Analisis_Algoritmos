
import pandas as pd

#Algori
def quicksort(lista, key):
    """
    Ordena una lista utilizando el algoritmo de quicksort,
    basado en el valor de una clave específica.

    Parámetros:
    ----------
    lista : list
        Lista de elementos que se desea ordenar.
    key : str
        Clave por la cual se compararán los elementos dentro de cada diccionario.

    Retorna:
    -------
    list
        Una nueva lista ordenada ascendentemente según el valor asociado a la clave `key`.
    """

    #Si la lista tiene 0 o 1 elemento devuelve la lista de la misma forma de como ingreso
    if len(lista) <= 1:
        return lista
    #Se escoje el pivote que es el elemento medio en la lista 
    pivote = lista[len(lista)//2]
    #Guardamos en la lista los elementos que sean menores a nuestro pivote
    menores = [x for x in lista if x[key] < pivote[key]]
    #Guardamos en la lista los elementos que sean iguales a nuestro pivote
    iguales = [x for x in lista if x[key] == pivote[key]]
    #Guardamos en la lista los elementos que sean mayores a nuestro pivote
    mayores = [x for x in lista if x[key] > pivote[key]]
    #Se vuelve a llamar la funcion recursivamente para que quede la lista organizada
    return quicksort(menores, key) + iguales + quicksort(mayores, key)


def mergesort(lista, key):
    """
    Ordena una lista utilizando el algoritmo de mergesort,
    basado en el valor de una clave específica.

    Parámetros:
    ----------
    lista : list
        Lista de elementos (como diccionarios) que se desea ordenar.
    key : str
        Clave por la cual se compararán los elementos dentro de cada diccionario.

    Retorna:
    -------
    list
        Una nueva lista ordenada ascendentemente según el valor asociado a la clave `key`.
    """
    #Si la lista es menor o igual a 1 devuelve la misma lista
    if len(lista) <= 1:
        return lista
    #Saca la mitad de la lista para tenerlo como referencia
    mitad = len(lista)//2
    #Toma los elementos de la lista desde donde inicia hasta la mitad
    izquierda = mergesort(lista[:mitad], key)
    #Toma los elementos desde la mitad hasta el final de la lista 
    derecha = mergesort(lista[mitad:], key)
    # Se vuelve a llamar la funcion hasta devolver la lista ordenada
    return merge(izquierda, derecha, key)

def merge(izquierda, derecha, key):
    """
    Combina dos listas ordenadas de diccionarios en una sola lista ordenada,
    comparando los valores según una clave específica.

    Parámetros:
    ----------
    izquierda : list
        Sublista ordenada de elementos (como diccionarios).
    derecha : list
        Otra sublista ordenada de elementos.
    key : str
        Clave por la cual se comparan los elementos para mantener el orden.

    Retorna:
    -------
    list
        Lista combinada y ordenada ascendentemente según el valor de la clave `key`.
    """
    #Lista vacia que va a ser llenada con los elementos de las dos listas que entran
    resultado = []
    i = j = 0
    #Mientras i sea menor al tamaño de las listas 
    while i < len(izquierda) and j < len(derecha):
        #Compara si la izquierda es menor que la derecha agrega en la izquierda
        if izquierda[i][key] <= derecha[j][key]:
            resultado.append(izquierda[i])
            i += 1
        #Sino agrega a la derecha 
        else:
            resultado.append(derecha[j])
            j += 1
    #Agregan lo que queda
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    #Devuelven una lista con el resultado
    return resultado

def ordenar_pedidos(path_csv, key="prioridad", metodo="quicksort"):
    """
    Ordena los registros de un archivo CSV que contiene pedidos, utilizando el algoritmo especificado
    y una clave de comparación determinada.

    Parámetros:
    ----------
    path_csv : str
        Ruta al archivo CSV que contiene los pedidos.
    key : str, opcional
        Clave por la cual se ordenarán los pedidos (por defecto: "prioridad").
    metodo : str, opcional
        Algoritmo de ordenamiento a utilizar: "quicksort" o "mergesort" (por defecto: "quicksort").

    Retorna:
    -------
    pandas.DataFrame
        DataFrame con los pedidos ordenados según la clave y el método especificado.

    """
    #Salida de nombre algoritmo
    print(f"Ordenando pedidos por medio del algoritmo de {metodo}")
    #Lee el archivo csv
    df = pd.read_csv(path_csv)
    #Convierte los datos a lista de diccionarios
    pedidos = df.to_dict("records")
    #Usa un selector para seleccionar el algoritmo a usar
    if metodo == "quicksort":
        ordenados = quicksort(pedidos, key)
    else:
        ordenados = mergesort(pedidos, key)
    #Devuelve los pedidos organizados como un nuevo dataframe
    return pd.DataFrame(ordenados)