import customtkinter as ctk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys
import os
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="#3a3a3a",
                foreground="white",
                rowheight=28,
                fieldbackground="#1a1a1a",
                font=("Segoe UI", 13))

style.map("Treeview",
          background=[("selected", "#3a7ee0")])

style.configure("Treeview.Heading",
                font=("Segoe UI", 14, "bold"),
                background="#333333",
                foreground="white")


# Agregar automáticamente la carpeta raíz del proyecto al PATH
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.append(ROOT)

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
        self.tabs = ctk.CTkTabview(
            self, 
            width=1150, 
            height=650,
            fg_color="#1b1b1b",  # FONDO OSCURO
            segmented_button_fg_color="#2b2b2b",
            segmented_button_selected_color="#3a7ee0",
            segmented_button_unselected_color="#444444",
            segmented_button_selected_hover_color="#2f6fc0"
        )
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
        import pandas as pd
        from modulos.ordenamiento import ordenar_pedidos
        from modulos.metricas import medir_rendimiento

        title = ctk.CTkLabel(self.tab_ordenamiento, text="Ordenamiento de Pedidos", font=("Arial", 22))
        title.pack(pady=10)

        # Selección del algoritmo
        self.algoritmo_orden = ctk.CTkComboBox(
            self.tab_ordenamiento,
            values=["quicksort", "mergesort"]
        )
        self.algoritmo_orden.set("quicksort")
        self.algoritmo_orden.pack(pady=10)

        # Botón ejecutar
        boton = ctk.CTkButton(
            self.tab_ordenamiento,
            text="Ordenar Pedidos",
            command=self.ejecutar_ordenamiento
        )
        boton.pack(pady=10)

        # Tabla (Treeview)
        self.tree_orden = ttk.Treeview(self.tab_ordenamiento, columns=("id", "destino", "prioridad", "peso"), show="headings", height=10)
        self.tree_orden.heading("id", text="ID")
        self.tree_orden.heading("destino", text="Destino")
        self.tree_orden.heading("prioridad", text="Prioridad")
        self.tree_orden.heading("peso", text="Peso")


        self.tree_orden.pack(pady=20)

        # Labels info
        self.label_tiempo_orden = ctk.CTkLabel(self.tab_ordenamiento, text="Tiempo: --")
        self.label_tiempo_orden.pack()

        self.label_memoria_orden = ctk.CTkLabel(self.tab_ordenamiento, text="Memoria: --")
        self.label_memoria_orden.pack()


    # ------------------ RUTAS ------------------

    def construir_tab_rutas(self):
        from modulos.rutas import construir_grafo

        title = ctk.CTkLabel(self.tab_rutas, text="Cálculo de Rutas (Dijkstra / A*)", font=("Segoe UI", 22, "bold"))
        title.pack(pady=10)

        # Cargar nodos
        G, posiciones = construir_grafo("informacion/rutas.csv")
        self.nodos = list(G.nodes)

        # ORIGEN
        self.combo_origen = ctk.CTkComboBox(self.tab_rutas, values=self.nodos)
        self.combo_origen.set(self.nodos[0])
        self.combo_origen.pack(pady=5)

        # DESTINO
        self.combo_destino = ctk.CTkComboBox(self.tab_rutas, values=self.nodos)
        self.combo_destino.set(self.nodos[-1])
        self.combo_destino.pack(pady=5)

        # Algoritmo
        self.combo_algoritmo_rutas = ctk.CTkComboBox(
            self.tab_rutas,
            values=["Dijkstra", "A*"]
        )
        self.combo_algoritmo_rutas.set("Dijkstra")
        self.combo_algoritmo_rutas.pack(pady=5)

        # Botón ejecutar
        btn = ctk.CTkButton(
            self.tab_rutas,
            text="Calcular Ruta Óptima",
            command=self.ejecutar_rutas
        )
        btn.pack(pady=10)

        # Resultado (texto)
        self.label_resultado_ruta = ctk.CTkLabel(self.tab_rutas, text="Distancia: --", font=("Segoe UI", 16))
        self.label_resultado_ruta.pack(pady=5)

        self.label_tiempo_rutas = ctk.CTkLabel(self.tab_rutas, text="Tiempo: --")
        self.label_tiempo_rutas.pack()

        self.label_memoria_rutas = ctk.CTkLabel(self.tab_rutas, text="Memoria: --")
        self.label_memoria_rutas.pack()

        # Marco para gráfica
        self.frame_rutas_grafica = ctk.CTkFrame(self.tab_rutas, width=900, height=400)
        self.frame_rutas_grafica.pack(pady=20)




    # ------------------ ASIGNACIÓN ------------------

    def construir_tab_asignacion(self):
        from modulos.asignacion import hungaro, greedy

        title = ctk.CTkLabel(self.tab_asignacion, text="Asignación de Recursos (Hungaro / Greedy)", font=("Arial", 22))
        title.pack(pady=10)

        # Botones para ejecutar los algoritmos
        frame_botones = ctk.CTkFrame(self.tab_asignacion)
        frame_botones.pack(pady=15)

        btn_hungaro = ctk.CTkButton(frame_botones, text="Ejecutar Húngaro", command=self.ejecutar_hungaro)
        btn_hungaro.grid(row=0, column=0, padx=10)

        btn_greedy = ctk.CTkButton(frame_botones, text="Ejecutar Greedy", command=self.ejecutar_greedy)
        btn_greedy.grid(row=0, column=1, padx=10)

        # Tabla de asignaciones
        self.tree_asignacion = ttk.Treeview(
            self.tab_asignacion, 
            columns=("vehiculo", "ruta", "costo"), 
            show="headings",
            height=10
        )
        self.tree_asignacion.heading("vehiculo", text="Vehículo")
        self.tree_asignacion.heading("ruta", text="Ruta")
        self.tree_asignacion.heading("costo", text="Costo")

        self.tree_asignacion.pack(pady=20)

        # Labels de resultados
        self.label_costo_asign = ctk.CTkLabel(self.tab_asignacion, text="Costo total: --")
        self.label_costo_asign.pack()

        self.label_tiempo_asign = ctk.CTkLabel(self.tab_asignacion, text="Tiempo: --")
        self.label_tiempo_asign.pack()

        self.label_memoria_asign = ctk.CTkLabel(self.tab_asignacion, text="Memoria: --")
        self.label_memoria_asign.pack()


    # ------------------ GRÁFICAS ------------------

    def construir_tab_graficas(self):
        title = ctk.CTkLabel(self.tab_graficas, text="Gráficas Comparativas", font=("Arial", 22))
        title.pack(pady=10)

        # Botón para actualizar la gráfica
        boton = ctk.CTkButton(self.tab_graficas, text="Generar Gráficas", command=self.mostrar_graficas)
        boton.pack(pady=10)

        # Frame para mostrar la gráfica
        self.frame_grafica = ctk.CTkFrame(self.tab_graficas, width=900, height=500)
        self.frame_grafica.pack(pady=20)



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

    #Funciones de ejecucion

    def ejecutar_ordenamiento(self):
        from modulos.metricas import medir_rendimiento
        from modulos.ordenamiento import ordenar_pedidos

        algoritmo = self.algoritmo_orden.get()

        # Ejecutar algoritmo
        (df, t, m) = medir_rendimiento(
            ordenar_pedidos,
            "informacion/pedidos.csv",
            key="prioridad",
            metodo=algoritmo
        )

        # Limpiar tabla
        for item in self.tree_orden.get_children():
            self.tree_orden.delete(item)

        # Insertar datos
        for _, row in df.iterrows():
            self.tree_orden.insert("", "end", values=(
                row["id"],
                row["destino"],
                row["prioridad"],
                row["peso"]
            ))

        # Mostrar métricas
        self.label_tiempo_orden.configure(text=f"Tiempo: {t:.6f} s")
        self.label_memoria_orden.configure(text=f"Memoria: {m} bytes")

    def ejecutar_rutas(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from modulos.rutas import construir_grafo, dijkstra, a_star
        from modulos.metricas import medir_rendimiento
        import networkx as nx

        origen = self.combo_origen.get()
        destino = self.combo_destino.get()
        algoritmo = self.combo_algoritmo_rutas.get()

        G, posiciones = construir_grafo("informacion/rutas.csv")

        # Ejecutar algoritmo con métricas
        if algoritmo == "Dijkstra":
            ((distancia, ruta), t, m) = medir_rendimiento(dijkstra, G, origen, destino)
        else:
            ((distancia, ruta), t, m) = medir_rendimiento(a_star, G, origen, destino, posiciones)

        # Mostrar información
        self.label_resultado_ruta.configure(text=f"Distancia óptima: {distancia}")
        self.label_tiempo_rutas.configure(text=f"Tiempo: {t:.6f} s")
        self.label_memoria_rutas.configure(text=f"Memoria: {m} bytes")

        # Limpiar gráfica previa
        for widget in self.frame_rutas_grafica.winfo_children():
            widget.destroy()

        # ---- DIBUJAR GRAFO ----
        fig, ax = plt.subplots(figsize=(7, 4))

        # Dibujar grafo general
        nx.draw(G, posiciones, with_labels=True, node_size=600, node_color="lightgray", ax=ax)

        # Dibujar ruta óptima
        if ruta and len(ruta) > 1:
            edges = list(zip(ruta, ruta[1:]))
            nx.draw_networkx_nodes(G, posiciones, nodelist=ruta, node_color="lightgreen", node_size=700, ax=ax)
            nx.draw_networkx_edges(G, posiciones, edgelist=edges, edge_color="green", width=3, ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=self.frame_rutas_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack()


    
    def ejecutar_hungaro(self):
        from modulos.asignacion import hungaro
        from modulos.metricas import medir_rendimiento
        import pandas as pd

        # Ejecutar con métricas
        (resultado, t, m) = medir_rendimiento(hungaro, "informacion/asignacion.csv")

        asignaciones, costo_total = resultado

        # Limpiar tabla
        for item in self.tree_asignacion.get_children():
            self.tree_asignacion.delete(item)

        # Insertar resultados
        for vehiculo, ruta in asignaciones:
            self.tree_asignacion.insert("", "end", values=(vehiculo, ruta, ""))

        # Mostrar resultados
        self.label_costo_asign.configure(text=f"Costo total: {costo_total}")
        self.label_tiempo_asign.configure(text=f"Tiempo: {t:.6f} s")
        self.label_memoria_asign.configure(text=f"Memoria: {m} bytes")

    def ejecutar_greedy(self):
        from modulos.asignacion import greedy
        from modulos.metricas import medir_rendimiento
        import pandas as pd

        # Ejecutar con métricas
        (resultado, t, m) = medir_rendimiento(greedy, "informacion/asignacion.csv")

        asignaciones, costo_total = resultado

        # Limpiar tabla
        for item in self.tree_asignacion.get_children():
            self.tree_asignacion.delete(item)

        # Insertar resultados
        for vehiculo, ruta in asignaciones:
            self.tree_asignacion.insert("", "end", values=(vehiculo, ruta, ""))

        # Mostrar resultados
        self.label_costo_asign.configure(text=f"Costo total: {costo_total}")
        self.label_tiempo_asign.configure(text=f"Tiempo: {t:.6f} s")
        self.label_memoria_asign.configure(text=f"Memoria: {m} bytes")

    def mostrar_graficas(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        # Limpiar gráfica previa
        for widget in self.frame_grafica.winfo_children():
            widget.destroy()

        # Cargar resultados
        df = pd.read_csv("resultados/comparativas.csv")

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        fig.tight_layout(pad=4)

        # ------------ Gráfica de tiempo ------------
        axes[0].bar(df["algoritmo"], df["tiempo_segundos"], color="skyblue")
        axes[0].set_title("Tiempo de ejecución")
        axes[0].set_ylabel("Segundos")
        axes[0].tick_params(axis='x', rotation=45)

        # ------------ Gráfica de memoria ------------
        axes[1].bar(df["algoritmo"], df["memoria_bytes"], color="lightgreen")
        axes[1].set_title("Uso de memoria")
        axes[1].set_ylabel("Bytes")
        axes[1].tick_params(axis='x', rotation=45)

        # Incrustar gráfica en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack()



if __name__ == "__main__":
    app = SistemaLogistica()
    app.mainloop()
