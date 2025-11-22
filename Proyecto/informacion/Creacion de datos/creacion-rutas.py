import csv
import random
from itertools import combinations

# ========================= CONFIGURACIÓN GRANDE =========================
num_ciudades = 80
num_conexiones = 200
min_distancia = 80
max_distancia = 520
archivo_salida = "grafo_80_ciudades_200_aristas.csv"

print(f"Generando grafo con {num_ciudades} ciudades y {num_conexiones} conexiones aleatorias...")

# Generamos todas las combinaciones posibles de pares (i,j) con i < j
todos_los_pares = list(combinations(range(1, num_ciudades + 1), 2))

# Barajamos y tomamos solo las primeras 200
random.shuffle(todos_los_pares)
conexiones_seleccionadas = todos_los_pares[:num_conexiones]

# Guardamos en CSV (muy rápido)
with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["origen", "destino", "distancia"])
    
    for i, (c1, c2) in enumerate(conexiones_seleccionadas, 1):
        origen = f"C{c1}"
        destino = f"C{c2}"
        distancia = random.randint(min_distancia, max_distancia)
        writer.writerow([origen, destino, distancia])
        
        # Progreso cada 50 aristas
        if i % 50 == 0 or i == num_conexiones:
            print(f"   → {i}/{num_conexiones} conexiones generadas...")

print(f"¡COMPLETADO!")
print(f"Grafo guardado en: {archivo_salida}")
print(f"   • Ciudades: {num_ciudades}")
print(f"   • Conexiones: {num_conexiones}")
print(f"   • Tamaño aproximado: ~6 KB")