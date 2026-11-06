import tkinter as tk

def mostrar():
    resultado.config(text=f"Turno elegido: {turno.get()}")

    #if turno.get() == 'Matutino':
    #    print('Es Matutino')


ventana = tk.Tk()
ventana.title("Turno")
ventana.geometry("280x150")

pregunta = tk.Label(ventana, text="¿En qué turno estás?")
pregunta.pack()
turno = tk.StringVar()
turno.set("Matutino")

opcion_matutino = tk.Radiobutton(ventana, text="Matutino", variable=turno, value="Matutino", command=mostrar)
opcion_matutino.pack()
opcion_vespertino = tk.Radiobutton(ventana, text="Vespertino", variable=turno, value="Vespertino", command=mostrar)
opcion_vespertino.pack()
boton = tk.Button(ventana, text="Mostrar", command=mostrar)
boton.pack()
resultado = tk.Label(ventana, text="")
resultado.pack()

mostrar()

ventana.mainloop()