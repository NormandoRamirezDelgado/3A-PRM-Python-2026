import tkinter as tk

def subir():
    puntos.set(puntos.get() + 5)
    print("Puntos:", puntos.get(), type(puntos.get()))

ventana = tk.Tk()
ventana.title("IntVar")

puntos = tk.IntVar()

marcador = tk.Label(ventana, textvariable=puntos, font=("Arial", 28))
marcador.pack()
boton = tk.Button(ventana, text="+5 puntos", command=subir)
boton.pack()

ventana.mainloop()