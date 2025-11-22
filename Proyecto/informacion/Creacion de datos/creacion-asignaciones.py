import csv
import random

# ========================= GRANDE: 100 vehículos × 100 rutas =========================
num_vehiculos = 100
num_rutas = 100
archivo_salida = "costo_vehiculo_ruta_100x100.csv"

print(f"Generando {num_vehiculos * num_rutas:,} combinaciones (100z100)...")

with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["vehiculo", "ruta", "costo"])

    contador = 0
    for v in range(1, num_vehiculos + 1):
        vehiculo = f"V{v}"
        for r in range(1, num_rutas + 1):
            ruta = f"R{r}"
            
            # Costo aleatorio realista entre 260 y 580
            costo_base = random.randint(260, 580)
            
            # Pequeño sesgo por vehículo y ruta para que no sea 100% plano (más real)
            sesgo_vehiculo = random.gauss(0, 18)   # algunos vehículos son sistemáticamente ± baratos
            sesgo_ruta     = random.gauss(0, 22)   # algunas rutas son ± caras
            costo = int(costo_base + sesgo_vehiculo + sesgo_ruta)
            
            # Aseguramos rango
            costo = max(260, min(580, costo))
            
            writer.writerow([vehiculo, ruta, costo])
            contador += 1
            
            # Progreso cada 2000 filas
            if contador % 2000 == 0:
                print(f"   → {contador:,}/10.000 generados...")

print(f"¡10.000 combinaciones generadas en menos de 1 segundo!")
print(f"Archivo listo: {archivo_salida}")
print(f"   • Tamaño aproximado: ~180 KB")