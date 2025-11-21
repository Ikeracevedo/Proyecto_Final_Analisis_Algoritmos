#Libreria time para incluir un medidor de tiempo para las ejecuciones
import time
#Libreria que me permite rastrear el paso y flujo de memoria
import tracemalloc
#Libreria para analizar y manipular los datos
import pandas as pd
#Libreria que me permite ejecutar comandos a la maquina directamente al sistema operativo 
import os

# Lista donde se daurdan los resultados de todos los algoritmos
resultados = []

def medir_rendimiento(funcion, *args, **kwargs):
    """
    Mide tiempo y memoria de ejecucion de una funcion.
    Retorna: (resultado, tiempo, memoria_pico)
    """

    #Iniciar contador de tiempo
    inicio_tiempo = time.perf_counter()

    #Iniciar la medicion de memoria
    tracemalloc.start()

    #Ejecutamos la funcion
    resultado = funcion(*args, **kwargs)

    #Obtener memoria pico
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    #Tiempo final
    fin_tiempo = time.perf_counter()
    duracion = fin_tiempo - inicio_tiempo

    return resultado, duracion, memoria_pico

def guardar_resultado(nombre_algoritmo, tiempo, memoria, extra=""):
    """
    Guarda los valores en una tabla interna que luego se exporta
    """

    resultados.append({
        "algoritmo": nombre_algoritmo,
        "tiempo_segundos": tiempo,
        "memoria_bytes": memoria,
        "extra": extra
    })

def exportar_csv(ruta="resultados/comparativas.csv"):
    """
    Exporta los resultados recopilados a un archivo CSV
    """

    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df = pd.DataFrame(resultados)
    df.to_csv(ruta, index=False)
    print(f"Resultados guardados en la ruta {ruta}")