
import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

def hungaro(path_csv):
    """
    Resuelve el problema de asignación óptima entre vehículos y rutas usando el algoritmo húngaro.

    Parámetros:
    ----------
    path_csv : str
        Ruta al archivo CSV que contiene las columnas 'vehiculo', 'ruta' y 'costo'.

    Retorna:
    -------
    tuple
        - Lista de asignaciones (vehiculo, ruta) según el orden óptimo.
        - Costo total mínimo de la asignación.
    """

    df = pd.read_csv(path_csv)
    matriz = df.pivot(index="vehiculo", columns="ruta", values="costo").to_numpy()
    fila, col = linear_sum_assignment(matriz)
    costo_total = matriz[fila, col].sum()

    return list(zip(df["vehiculo"].unique(), df["ruta"].unique())), costo_total

def greedy(path_csv):
    """
    Resuelve el problema de asignación entre vehículos y rutas usando un enfoque voraz (greedy),
    seleccionando las combinaciones de menor costo disponibles sin repetir vehículo ni ruta.

    Parámetros:
    ----------
    path_csv : str
        Ruta al archivo CSV que contiene las columnas 'vehiculo', 'ruta' y 'costo'.

    Retorna:
    -------
    tuple
        - Lista de asignaciones (vehiculo, ruta) seleccionadas.
        - Costo total acumulado de las asignaciones.
    """

    df = pd.read_csv(path_csv)
    df = df.sort_values("costo")
    asignados_veh = set()
    asignados_ruta = set()
    total = 0
    asignaciones = []
    for _, fila in df.iterrows():
        if fila["vehiculo"] not in asignados_veh and fila["ruta"] not in asignados_ruta:
            asignados_veh.add(fila["vehiculo"])
            asignados_ruta.add(fila["ruta"])
            total += fila["costo"]
            asignaciones.append((fila["vehiculo"], fila["ruta"]))
    return asignaciones, total