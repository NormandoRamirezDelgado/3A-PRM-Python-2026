import ttkbootstrap as tb

def mostrar():
    resultado.config(text=f"Turno elegido: {turno.get()}")


ventana = tb.Window()
ventana.title("Turno")
ventana.geometry("280x150")
pregunta = tb.Label(ventana, text="¿En qué turno estás?")
pregunta.pack()
turno = tb.StringVar()
turno.set("matutino")

opcion_matutino = tb.Radiobutton(ventana, text="Matutino", variable=turno, value="matutino")
opcion_matutino.pack()
opcion_vespertino = tb.Radiobutton(ventana, text="Vespertino", variable=turno, value="vespertino")
opcion_vespertino.pack()
boton = tb.Button(ventana, text="Mostrar", command=mostrar)
boton.pack()
resultado = tb.Label(ventana, text="")
resultado.pack()

ventana.mainloop()