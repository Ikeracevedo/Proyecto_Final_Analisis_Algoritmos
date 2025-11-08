# main.py
from modulos.ordenamiento import ordenar_pedidos
from modulos.rutas import construir_grafo, dijkstra
from modulos.asignacion import hungaro

def main():
    print("=== SISTEMA DE OPTIMIZACIÓN LOGÍSTICA ===")

    print("\n1️⃣ Ordenando pedidos...")
    pedidos_ordenados = ordenar_pedidos("informacion/pedidos.csv", key="prioridad", metodo="quicksort")
    print(pedidos_ordenados.head())

    print("\n2️⃣ Calculando ruta óptima...")
    G = construir_grafo("informacion/rutas.csv")
    distancia = dijkstra(G, "A", "E")
    print(f"Ruta más corta de A a E: {distancia} km")

    print("\n3️⃣ Asignando recursos (Algoritmo Húngaro)...")
    asignaciones, costo = hungaro("informacion/asignacion.csv")
    print(f"Asignaciones: {asignaciones}")
    print(f"Costo total: {costo}")

if __name__ == "__main__":
    main()
