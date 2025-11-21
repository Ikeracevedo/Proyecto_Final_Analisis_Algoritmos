import pandas as pd
import matplotlib.pyplot as plt
import os

def graficar_resultados(path_csv="resultados/comparativas.csv"):
    df = pd.read_csv(path_csv)

    # Crear carpeta si no existe
    os.makedirs("resultados/graficas", exist_ok=True)

    # --- Gráfica de tiempo ---
    plt.figure(figsize=(8,5))
    plt.bar(df["algoritmo"], df["tiempo_segundos"], color="skyblue")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de tiempo entre algoritmos")
    plt.savefig("resultados/graficas/tiempo.png")
    plt.close()

    # --- Gráfica de memoria ---
    plt.figure(figsize=(8,5))
    plt.bar(df["algoritmo"], df["memoria_bytes"], color="lightgreen")
    plt.ylabel("Memoria (bytes)")
    plt.title("Comparación de memoria entre algoritmos")
    plt.savefig("resultados/graficas/memoria.png")
    plt.close()

    print("📊 Gráficas generadas en resultados/graficas/")
