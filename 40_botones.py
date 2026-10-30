import tkinter as tk

def saludar():
    print("¡Hola! Me diste clic")

def calcular():
    print(f'{5*4}')


ventana = tk.Tk()
ventana.title("Mi primer botón")
ventana.geometry("300x100")
boton = tk.Button(ventana, text="Saludar", command=calcular)
boton.pack()

ventana.mainloop()