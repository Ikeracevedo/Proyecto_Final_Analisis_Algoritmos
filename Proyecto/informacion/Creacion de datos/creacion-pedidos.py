import csv
import random
from datetime import datetime

# ========================= CONFIGURACIÓN =========================
num_pedidos = 50_000
archivo_salida = "pedidos_50000.csv"

# Lista de 25 ciudades colombianas reales (puedes agregar más si quieres)
ciudades = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira",
    "Santa Marta", "Cúcuta", "Ibagué", "Villavicencio", "Pasto", "Manizales", "Neiva",
    "Montería", "Valledupar", "Sincelejo", "Popayán", "Armenia", "Riohacha",
    "Tunja", "Florencia", "Quibdó", "Ipiales", "Mitú"
]

# Semilla opcional para resultados reproducibles (quítala si quieres pura aleatoriedad)
# random.seed(42)

print(f"Generando {num_pedidos:,} pedidos...")

# Usamos 'with' + writerow en lote para máxima velocidad
with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "destino", "prioridad", "peso"])  # Cabecera

    for id_pedido in range(1, num_pedidos + 1):
        destino = random.choice(ciudades)
        prioridad = random.randint(1, 5)
        peso = round(random.uniform(4.5, 24.9), 1)   # entre 4.5 y 24.9 kg
        
        writer.writerow([id_pedido, destino, prioridad, peso])

        # Mostrar progreso cada 10.000 pedidos
        if id_pedido % 10_000 == 0:
            print(f"   → {id_pedido:,} pedidos generados...")

print(f"¡Listo! 50.000 pedidos guardados en → {archivo_salida}")
print(f"Tamaño aproximado del archivo: ~3.2 MB")