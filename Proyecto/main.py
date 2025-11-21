# main.py
from modulos.ordenamiento import ordenar_pedidos
from modulos.rutas import construir_grafo, dijkstra, a_star
from modulos.asignacion import greedy, hungaro
from modulos.metricas import medir_rendimiento, guardar_resultado, exportar_csv
from modulos.graficas import graficar_resultados


def main():
    print("=== SISTEMA DE OPTIMIZACIÓN LOGÍSTICA ===")

# 1. ORDENAMIENTO
    print("\n Ordenando pedidos...")
    #Algoritmo QuickSort
    (_, t, m) = medir_rendimiento(
        ordenar_pedidos,
        "informacion/pedidos.csv",
        key="prioridad",
        metodo="quicksort"
    )
    guardar_resultado("QuickSort", t, m, "pedidos.csv")

    #Algoritmo MergeSort
    (_, t, m) = medir_rendimiento(
        ordenar_pedidos,
        "informacion/pedidos.csv",
        key="prioridad",
        metodo="mergesort"
    )
    guardar_resultado("MergeSort", t, m, "pedidos.csv")

# 2. RUTAS
    print("\n Calculando ruta óptima...")
    
    G, posiciones = construir_grafo("informacion/rutas.csv")
    # Elegir dos nodos válidos automáticamente
    nodos = list(G.nodes())
    origen = nodos[0]
    destino = nodos[-1]

    # Dijkstra
    (_, t, m) = medir_rendimiento(dijkstra, G, origen, destino)
    guardar_resultado("Dijkstra", t, m, "rutas.csv")

    # A*
    (_, t, m) = medir_rendimiento(a_star, G, origen, destino, posiciones)
    guardar_resultado("A*", t, m, "rutas.csv")


# 3. ASIGNACIÓN

    # Húngaro
    (_, t, m) = medir_rendimiento(hungaro, "informacion/asignacion.csv")
    guardar_resultado("Hungaro", t, m, "asignacion.csv")

    # Greedy
    (_, t, m) = medir_rendimiento(greedy, "informacion/asignacion.csv")
    guardar_resultado("Greedy", t, m, "asignacion.csv")

# 4. EXPORTAR RESULTADOS
    exportar_csv("resultados/comparativas.csv")

    graficar_resultados("resultados/comparativas.csv")

if __name__ == "__main__":
    main()
