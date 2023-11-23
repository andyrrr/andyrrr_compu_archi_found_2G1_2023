import tkinter as tk
from tkinter import ttk

def cambiar_imagen():
    opcion = dropdown.get()
    ruta_imagen = ""

    if opcion == "Procesador uniciclo":
        ruta_imagen = "imagenes/uniciclo.png"
    elif opcion == "Procesador multiciclo":
        ruta_imagen = "imagenes/Multiciclo.png"
    elif opcion == "Procesador Segmentado":
        ruta_imagen = "imagenes/pipeline.png"
    elif opcion == "Procesador Segmentado con Adelantamiento":
        ruta_imagen = "imagenes/hazard.png"

    imagen.configure(image=tk.PhotoImage(file=ruta_imagen))
    imagen.image = tk.PhotoImage(file=ruta_imagen)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulador")

# Dropdown




# Radiobuttons
modo_funcionamiento = tk.StringVar()
modo_funcionamiento.set("Ejecución Completa")

radiobutton1 = tk.Radiobutton(ventana, text="Step by Step", variable=modo_funcionamiento, value="Radio 1")
radiobutton2 = tk.Radiobutton(ventana, text="Unidad de tiempo", variable=modo_funcionamiento, value="Radio 2")
radiobutton3 = tk.Radiobutton(ventana, text="Ejecución Completa", variable=modo_funcionamiento, value="Radio 3")

radiobutton1.grid(row=1, column=0, sticky="w", padx=10, pady=5)
radiobutton2.grid(row=2, column=0, sticky="w", padx=10, pady=5)
radiobutton3.grid(row=3, column=0, sticky="w", padx=10, pady=5)

# Imagen
imagen = tk.Label(ventana)
imagen.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

# Formulario
formulario_label = tk.Label(ventana, text="Estadísticas:")
formulario_label.grid(row=4, column=0, columnspan=2, pady=5)

campo1_label = tk.Label(ventana, text="Campo 1:")
campo1_label.grid(row=5, column=0, pady=5)

campo1_entry = tk.Entry(ventana)
campo1_entry.grid(row=5, column=1, pady=5)

campo2_label = tk.Label(ventana, text="Campo 2:")
campo2_label.grid(row=6, column=0, pady=5)

campo2_entry = tk.Entry(ventana)
campo2_entry.grid(row=6, column=1, pady=5)

# Botón "Start"
start_button = tk.Button(ventana, text="Comenzar", command=cambiar_imagen)
start_button.grid(row=7, column=0, columnspan=2, pady=10)

# Mostrar la ventana
ventana.mainloop()
