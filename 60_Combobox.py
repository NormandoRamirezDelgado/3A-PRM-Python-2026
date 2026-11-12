import ttkbootstrap as tb

def mostrar():
    resultado.config(text=f"Elegiste: {lista.get()}")


ventana = tb.Window()

ventana.title("Carrera")
ventana.geometry("320x150")

pregunta = tb.Label(ventana, text="¿Qué carrera estudias?")
pregunta.pack()
carreras = ['Electricidad', "Programación", "Contabilidad", "Electrónica", "Mecatrónica", 'Inteligencia Artificial']

lista = tb.Combobox(ventana, values=carreras, state="readonly", width=20)
lista.current(0)
lista.pack()
boton = tb.Button(ventana, text="Mostrar", command=mostrar)
boton.pack()
resultado = tb.Label(ventana, text="")
resultado.pack()

ventana.mainloop()