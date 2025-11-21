import customtkinter as ctk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Configuración inicial
ctk.set_appearance_mode("dark")        # dark, light, system
ctk.set_default_color_theme("blue")    # blue, green, dark-blue


class SistemaLogistica(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Optimización Logística – Multialgorítmico")
        self.geometry("1200x700")
        self.resizable(False, False)

        # Crear notebook (pestañas)
        self.tabs = ctk.CTkTabview(self, width=1150, height=650)
        self.tabs.pack(pady=20)

        # Crear cada pestaña
        self.tab_ordenamiento = self.tabs.add("Ordenamiento")
        self.tab_rutas = self.tabs.add("Rutas")
        self.tab_asignacion = self.tabs.add("Asignación")
        self.tab_graficas = self.tabs.add("Gráficas")
        self.tab_info = self.tabs.add("Información")

        # Construcción interna de cada pestaña
        self.construir_tab_ordenamiento()
        self.construir_tab_rutas()
        self.construir_tab_asignacion()
        self.construir_tab_graficas()
        self.construir_tab_info()


    # ------------------ ORDENAMIENTO ------------------

    def construir_tab_ordenamiento(self):
        label = ctk.CTkLabel(self.tab_ordenamiento, text="Ordenamiento de Pedidos", font=("Arial", 22))
        label.pack(pady=20)

        # Aquí luego pondremos:
        # - dropdown de algoritmo
        # - boton ejecutar
        # - tabla resultados
        # - labels de tiempo/memoria


    # ------------------ RUTAS ------------------

    def construir_tab_rutas(self):
        label = ctk.CTkLabel(self.tab_rutas, text="Cálculo de Rutas (Dijkstra / A*)", font=("Arial", 22))
        label.pack(pady=20)

        # Aquí luego agregaremos:
        # - dropdown de origen/destino
        # - seleccionar algoritmo
        # - boton ejecutar
        # - mostrar resultado
        # - gráfica de rutas (opcional)


    # ------------------ ASIGNACIÓN ------------------

    def construir_tab_asignacion(self):
        label = ctk.CTkLabel(self.tab_asignacion, text="Asignación de Recursos (Hungaro / Greedy)", font=("Arial", 22))
        label.pack(pady=20)


    # ------------------ GRÁFICAS ------------------

    def construir_tab_graficas(self):
        label = ctk.CTkLabel(self.tab_graficas, text="Gráficas Comparativas", font=("Arial", 22))
        label.pack(pady=20)


    # ------------------ INFORMACIÓN ------------------

    def construir_tab_info(self):
        texto = """
Sistema de Optimización Logística Multialgorítmico
Desarrollado por: Iker 🌟

Incluye:
- QuickSort / MergeSort
- Dijkstra / A*
- Húngaro / Greedy
- Métricas de tiempo y memoria
- Gráficas automáticas

Universidad Sergio Arboleda - Análisis de Algoritmos
2025
"""
        info_label = ctk.CTkLabel(self.tab_info, text=texto, justify="left", font=("Arial", 16))
        info_label.pack(pady=40)


if __name__ == "__main__":
    app = SistemaLogistica()
    app.mainloop()
