import ttkbootstrap as tb

def saludar():
    nombre = entrada.get()
    resultado.config(text=f"¡Hola, {nombre}!")


def limpiar():
    entrada.delete(0, "end")
    resultado.config(text="")

ventana = tb.Window()
ventana.title("Saludo")
ventana.geometry("300x150")
pregunta = tb.Label(ventana, text="¿Cómo te llamas?")
pregunta.pack()
entrada = tb.Entry(ventana, width=25)
entrada.pack()
boton = tb.Button(ventana, text="Saludar", command=saludar)
boton.pack()
borrar = tb.Button(ventana, text="Limpiar", command=limpiar)
borrar.pack()
resultado = tb.Label(ventana, text="", font=("Arial", 14))
resultado.pack()

ventana.mainloop()