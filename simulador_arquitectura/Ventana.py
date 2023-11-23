import time
from tkinter import *
from tkinter.ttk import Combobox, Treeview


def iniciar_simulacion():
    arquitectura = dropdown.get()
    modo = modo_funcionamiento.get()
    print (arquitectura)
    print(modo)

    global ciclo_actual, pc_actual, tiempo_inicial
    ciclo_actual = 3
    tiempo_inicial = time.time()
    pc_actual = 0x0003
    # Actualizar la información periódicamente
    actualizar_informacion()

def actualizar_informacion():
    tiempo_total = time.time() - tiempo_inicial
    ciclo_ejecucion.set(str(ciclo_actual))
    tiempo_ejecucion.set("{:.2f}".format(tiempo_total))
    valor_pc.set("0x{:X}".format(pc_actual))

    for reg in registros:
        tabla_registros.insert("", END, values=reg)

    for mem in memoria:
        tabla_memoria.insert("", END, values=mem)

    root.update()

def cargar_imagen(ruta_imagen):
    imagen = PhotoImage(file=ruta_imagen).subsample(2)
    return imagen

def actualizar_imagen(event, etiqueta):
    # Obtener el valor seleccionado del Combobox
    opcion = dropdown.get()
    ruta_imagen = ""
    if opcion == "Procesador uniciclo":
        ruta_imagen = "./imagenes/uniciclo.png"
    elif opcion == "Procesador multiciclo":
        ruta_imagen = "./imagenes/Multiciclo.png"
    elif opcion == "Procesador Segmentado":
        ruta_imagen = "./imagenes/pipeline.png"
    elif opcion == "Procesador Segmentado con Adelantamiento":
        ruta_imagen = "./imagenes/hazard.png"

    nueva_imagen = cargar_imagen(ruta_imagen)
    etiqueta.configure(image=nueva_imagen)
    etiqueta.image = nueva_imagen
    root.update()



root = Tk()
root.geometry("1200x600")

# Frame superior
opciones_frame = Frame(root,  height=200)
opciones_frame.pack(fill="both", expand=True)

of1 = Frame(opciones_frame,  width=200)
of1.pack(side="left", fill="both", expand=True)
of2 = Frame(opciones_frame,  width=200)
of2.pack(side="left", fill="both", expand=True)
of3 = Frame(opciones_frame, width=200)
of3.pack(side="left", fill="both", expand=True)

# Frame medio
imagen_frame = Frame(root, height=200)
imagen_frame.pack(fill="both", expand=True)



opciones = ["Procesador uniciclo", "Procesador multiciclo", "Procesador Segmentado",
            "Procesador Segmentado con Adelantamiento"]


image = PhotoImage(file="./imagenes/pipeline.png").subsample(2)
etiqueta = Label(imagen_frame, image=image)
etiqueta.pack()

dropdown = Combobox(of1, values=opciones)
dropdown.pack()
dropdown.bind("<<ComboboxSelected>>", lambda event: actualizar_imagen(event, etiqueta))
dropdown.set(opciones[0])  # Establecer el valor predeterminado



modo_funcionamiento = StringVar()
modo_funcionamiento.set("Ejecución Completa")

radiobutton1 = Radiobutton(of2, text="Step by Step", variable=modo_funcionamiento, value="step")
radiobutton2 = Radiobutton(of2, text="Unidad de tiempo", variable=modo_funcionamiento, value="tiempo")
radiobutton3 = Radiobutton(of2, text="Ejecución Completa", variable=modo_funcionamiento, value="completo")
radiobutton3.select()

radiobutton1.grid(row=1, column=0, sticky="w", padx=10, pady=5)
radiobutton2.grid(row=2, column=0, sticky="w", padx=10, pady=5)
radiobutton3.grid(row=3, column=0, sticky="w", padx=10, pady=5)


# Frame inferior
estadisticas_frame = Frame(root, bg="blue", height=200)
estadisticas_frame.pack(fill="both", expand=True)

ef1 = Frame(estadisticas_frame,  width=200)
ef1.pack(side="left", fill="both", expand=True)
ef2 = Frame(estadisticas_frame,  width=200)
ef2.pack(side="left", fill="both", expand=True)
ef3 = Frame(estadisticas_frame, width=200)
ef3.pack(side="left", fill="both", expand=True)

# Variables para almacenar la información
ciclo_ejecucion = StringVar()
tiempo_ejecucion = StringVar()
valor_pc = StringVar()

# Etiquetas para mostrar la información
ciclo_l = Label(ef1, text="Ciclo de Ejecución:").pack(pady=5)
ciclo_t = Label(ef1, textvariable=ciclo_ejecucion).pack(pady=5)

tiempo_l = Label(ef1, text="Tiempo desde el Inicio (s):").pack(pady=5)
tiempo_t = Label(ef1, textvariable=tiempo_ejecucion).pack(pady=5)

pc_l = Label(ef1, text="Valor del PC:").pack(pady=5)
pc_t = Label(ef1, textvariable=valor_pc).pack(pady=5)


Label(ef2, text="Registros").pack(pady=5, side='top')
Label(ef3, text="Memoria").pack(pady=5, side='top')


# Crear un Treeview con dos columnas
tabla_registros = Treeview(ef2, columns=("Label", "Valor"), show="headings")
tabla_registros.heading("Label", text="Registro")
tabla_registros.heading("Valor", text="Valor")
tabla_registros.pack(pady=10, side='left')


# Crear un Treeview con dos columnas
tabla_memoria = Treeview(ef3, columns=("Label", "Valor"), show="headings")
tabla_memoria.heading("Label", text="Memoria")
tabla_memoria.heading("Valor", text="Valor")
tabla_memoria.pack(pady=10, side='left')

# Agregar elementos al Treeview
memoria = []


# Agregar elementos al Treeview
registros = []


for i in range(32):
    nuevo_elemento = ("x" + str(i),"Vacio")
    registros.append(nuevo_elemento)


for i in range(1000):
    nuevo_elemento = ("0x" + str(i),"Vacio")
    memoria.append(nuevo_elemento)


# Botón "Start"
start_button = Button(of3, text="Comenzar", command=iniciar_simulacion)
start_button.pack()



root.mainloop()
