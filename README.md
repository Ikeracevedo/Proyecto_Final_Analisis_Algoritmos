# 🚚 Sistema de Optimización Logística Multialgorítmico

**Proyecto final – Análisis de Algoritmos**  
Universidad Sergio Arboleda – 2025

---

## 📝 Descripción General

Este proyecto implementa un sistema completo de optimización logística, diseñado para evaluar y comparar el rendimiento de diversos algoritmos esenciales en:

- Ordenamiento de pedidos
- Cálculo de rutas óptimas
- Asignación de recursos
- Generación automática de métricas
- Visualización gráfica de resultados
- Interfaz gráfica interactiva (GUI)

El sistema permite cargar datasets pequeños, medianos o grandes, ejecutar los algoritmos seleccionados, medir el desempeño real (tiempo y memoria), visualizar tablas, grafos y generar gráficas comparativas para análisis académico o técnico.

---

## 🚀 Características Principales

### 🔹 1. Módulo de Ordenamiento

**Incluye:**
- QuickSort
- MergeSort

Permite ordenar pedidos según prioridad o cualquier columna seleccionada. Se registran métricas de tiempo y memoria.

### 🔹 2. Módulo de Rutas

**Algoritmos implementados:**
- Dijkstra
- A* (A-star) con heurística euclidiana

**Funcionalidades:**
- Cálculo del camino más corto
- Construcción automática del grafo desde CSV
- Visualización del grafo y de la ruta óptima

### 🔹 3. Módulo de Asignación

**Incluye dos enfoques:**
- Algoritmo Húngaro (óptimo)
- Greedy (heurístico)

Permite resolver el problema de asignación de costos vehículo–ruta.

### 🔹 4. Métricas Automáticas

El sistema mide:
- Tiempo de ejecución (segundos)
- Memoria utilizada (bytes)
- Dataset asociado

Los resultados se almacenan en: `resultados/comparativas.csv`

### 🔹 5. Gráficas Automáticas

Se generan gráficas comparativas con:
- Tiempos de ejecución
- Uso de memoria

Las gráficas se guardan en: `resultados/graficas/`

### 🔹 6. Interfaz Gráfica (CustomTkinter)

Interfaz moderna, intuitiva y funcional:
- Pestaña de ordenamiento
- Pestaña de rutas
- Pestaña de asignación
- Pestaña de gráficas
- Pestaña de información del sistema

---

## 📁 Estructura del Proyecto

```
Proyecto/
│
├── informacion/
│   ├── pedidos.csv
│   ├── rutas.csv
│   └── asignacion.csv
│
├── modulos/
│   ├── ordenamiento.py
│   ├── rutas.py
│   ├── asignacion.py
│   └── metricas.py
│
├── interfaz/
│   └── gui.py
│
├── resultados/
│   ├── comparativas.csv
│   └── graficas/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

### 2. Crear ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución del Proyecto

### 🔸 Ejecutar versión por consola

```bash
python main.py
```

### 🔸 Ejecutar la interfaz gráfica

```bash
python interfaz/gui.py
```

---

## 📊 Datasets Incluidos

El proyecto incluye tres tamaños de dataset:

| Categoría | Tamaño | Uso |
|-----------|--------|-----|
| Pequeño | 4–10 filas | Pruebas rápidas |
| Mediano | 1.000–5.000 filas | Análisis intermedio |
| Grande | 10.000–50.000 filas y grafos con 80+ nodos | Pruebas de rendimiento |

También se incluye un generador automático de datasets grandes.

---

## 🧪 Resultados Experimentales

Los resultados completos (tiempo y memoria) se generan automáticamente y se pueden visualizar:

- En consola
- En la interfaz gráfica
- En el archivo `comparativas.csv`
- En las gráficas guardadas dentro de `resultados/graficas/`

**Ejemplo de columnas registradas:**  
`algoritmo, tiempo_segundos, memoria_bytes, extra`

---

## 📌 Tecnologías Utilizadas

- Python 3.13
- Pandas
- NetworkX
- Matplotlib
- CustomTkinter
- NumPy

---

## 👨‍💻 Autor

**Iker Acevedo Vargas**  
Universidad Sergio Arboleda  
Proyecto final – Análisis de Algoritmos (2025)

---

## 📚 Referencias

- Cormen, T., Leiserson, C., Rivest, R., & Stein, C. (2009). *Introduction to Algorithms*.
- Hart, P., Nilsson, N., & Raphael, B. (1968). *A Formal Basis for the Heuristic Determination of Minimum Cost Paths*.
- Kuhn, H. (1955). *The Hungarian Method for the Assignment Problem*.
- NetworkX, Pandas, Matplotlib, CustomTkinter — documentación oficial.

---

## ⭐ Contribuciones

Pull requests, issues y mejoras son bienvenidas.  
Este proyecto es de carácter académico pero está diseñado para ser escalable y extensible.
