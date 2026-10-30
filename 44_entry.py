import tkinter as tk

def saludar():
    nombre = entrada.get()
    resultado.config(text=f"¡Hola, {nombre}!")


def limpiar():
    entrada.delete(0, tk.END)
    resultado.config(text="")


ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("300x150")

pregunta = tk.Label(ventana, text="¿Cómo te llamas?")
pregunta.pack()
entrada = tk.Entry(ventana, width=25)
entrada.pack()
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()
borrar = tk.Button(ventana, text="Limpiar", command=limpiar)
borrar.pack()
resultado = tk.Label(ventana, text=" ", font=("Arial", 14,))
resultado.pack()

ventana.mainloop()