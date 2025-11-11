
import networkx as nx
import pandas as pd
import math
from queue import PriorityQueue

def construir_grafo(path_csv):
    """
    Construye un grafo no dirigido a partir de un archivo CSV con columnas: 'origen', 'destino' y 'distancia'.

    Parámetros:
    ----------
    path_csv : str
        Ruta al archivo CSV que contiene las conexiones entre nodos y sus distancias.

    Retorna:
    -------
    networkx.Graph
        Grafo con nodos conectados por aristas ponderadas (distancia).
    """
    df = pd.read_csv(path_csv)
    G = nx.Graph()
    for _, fila in df.iterrows():
        G.add_edge(fila["origen"], fila["destino"], weight=fila["distancia"])
    return G

def dijkstra(G, origen, destino):
    """
    Calcula la distancia mínima entre dos nodos usando el algoritmo de Dijkstra.

    Parámetros:
    ----------
    G : networkx.Graph
        Grafo con pesos en las aristas.
    origen : hashable
        Nodo de inicio.
    destino : hashable
        Nodo de destino.

    Retorna:
    -------
    float
        Costo mínimo desde el nodo origen hasta el nodo destino.
    """
    print("Calculando la ruta mas optima por medio del algoritmo de Dijkstra")
    dist = {nodo: float("inf") for nodo in G.nodes}
    dist[origen] = 0
    cola = PriorityQueue()
    cola.put((0, origen))
    visitados = {}

    while not cola.empty():
        (costo, actual) = cola.get()
        if actual in visitados:
            continue
        visitados[actual] = True
        for vecino in G.neighbors(actual):
            peso = G[actual][vecino]['weight']
            nuevo_costo = costo + peso
            if nuevo_costo < dist[vecino]:
                dist[vecino] = nuevo_costo
                cola.put((nuevo_costo, vecino))
    return dist[destino]

def heuristica(a, b, posiciones):
    """
    Calcula la distancia euclidiana entre dos nodos, usada como heurística para A*.

    Parámetros:
    ----------
    a, b : hashable
        Nombres de los nodos.
    posiciones : dict
        Diccionario con coordenadas (x, y) de cada nodo.

    Retorna:
    -------
    float
        Distancia euclidiana entre los nodos a y b.
    """
    print("Calculando la ruta mas optima de forma heuristica")
    (x1, y1), (x2, y2) = posiciones[a], posiciones[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def a_star(G, origen, destino, posiciones):
    """
    Calcula el costo mínimo entre dos nodos usando el algoritmo A* con heurística euclidiana.

    Parámetros:
    ----------
    G : networkx.Graph
        Grafo con pesos en las aristas.
    origen : hashable
        Nodo de inicio.
    destino : hashable
        Nodo de destino.
    posiciones : dict
        Diccionario con coordenadas (x, y) de cada nodo.

    Retorna:
    -------
    float or None
        Costo mínimo desde el nodo origen hasta el nodo destino, o None si no hay camino.
    """

    open_set = PriorityQueue()
    open_set.put((0, origen))
    came_from = {}
    g_score = {n: float("inf") for n in G.nodes}
    g_score[origen] = 0
    f_score = {n: float("inf") for n in G.nodes}
    f_score[origen] = heuristica(origen, destino, posiciones)

    while not open_set.empty():
        _, actual = open_set.get()
        if actual == destino:
            return g_score[actual]
        for vecino in G.neighbors(actual):
            tentative_g = g_score[actual] + G[actual][vecino]['weight']
            if tentative_g < g_score[vecino]:
                came_from[vecino] = actual
                g_score[vecino] = tentative_g
                f_score[vecino] = tentative_g + heuristica(vecino, destino, posiciones)
                open_set.put((f_score[vecino], vecino))
    return None