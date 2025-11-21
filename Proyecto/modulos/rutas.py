import networkx as nx
import pandas as pd
import math
from queue import PriorityQueue


# ============================================================
#   CONSTRUIR EL GRAFO DESDE CSV
# ============================================================

def construir_grafo(path_csv):
    df = pd.read_csv(path_csv)
    G = nx.Graph()

    # Cargar aristas
    for _, fila in df.iterrows():
        G.add_edge(fila["origen"], fila["destino"], weight=fila["distancia"])

    # Crear posiciones seguras y limpias para TODOS los nodos
    posiciones = {}
    nodos = list(G.nodes())

    import math
    n = len(nodos)
    radio = 3  # tamaño del círculo

    for i, nodo in enumerate(nodos):
        ang = 2 * math.pi * i / n
        posiciones[nodo] = (radio * math.cos(ang), radio * math.sin(ang))

    return G, posiciones


# ============================================================
#   DIJKSTRA (DISTANCIA + RUTA)
# ============================================================

def dijkstra(G, origen, destino):
    print("Calculando la ruta más óptima por medio del algoritmo de Dijkstra")

    import heapq

    dist = {n: float("inf") for n in G.nodes()}
    dist[origen] = 0

    padre = {n: None for n in G.nodes()}

    pq = [(0, origen)]

    while pq:
        costo, actual = heapq.heappop(pq)

        if actual == destino:
            break

        for vecino in G.neighbors(actual):
            peso = G[actual][vecino]["weight"]
            nuevo_costo = costo + peso

            if nuevo_costo < dist[vecino]:
                dist[vecino] = nuevo_costo
                padre[vecino] = actual
                heapq.heappush(pq, (nuevo_costo, vecino))

    # reconstruir ruta
    ruta = []
    nodo = destino

    while nodo is not None:
        ruta.append(nodo)
        nodo = padre[nodo]

    ruta.reverse()

    return dist[destino], ruta


# ============================================================
#   HEURÍSTICA EUCLIDIANA PARA A*
# ============================================================

def heuristica(a, b, posiciones):
    (x1, y1) = posiciones[a]
    (x2, y2) = posiciones[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# ============================================================
#   A* (DISTANCIA + RUTA)
# ============================================================

def a_star(G, origen, destino, posiciones):
    print("Calculando la ruta más óptima de forma heurística (A*)")

    open_set = PriorityQueue()
    open_set.put((0, origen))

    came_from = {}

    g_score = {n: float("inf") for n in G.nodes()}
    g_score[origen] = 0

    f_score = {n: float("inf") for n in G.nodes()}
    f_score[origen] = heuristica(origen, destino, posiciones)

    while not open_set.empty():
        _, actual = open_set.get()

        if actual == destino:
            ruta = [destino]
            while actual in came_from:
                actual = came_from[actual]
                ruta.append(actual)
            ruta.reverse()
            return g_score[destino], ruta

        for vecino in G.neighbors(actual):
            tentative_g = g_score[actual] + G[actual][vecino]["weight"]

            if tentative_g < g_score[vecino]:
                came_from[vecino] = actual
                g_score[vecino] = tentative_g
                f_score[vecino] = tentative_g + heuristica(vecino, destino, posiciones)
                open_set.put((f_score[vecino], vecino))

    return float("inf"), []
