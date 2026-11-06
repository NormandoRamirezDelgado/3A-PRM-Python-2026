import tkinter as tk

def poner_ejemplo():
    nombre.set("Ana López")


ventana = tk.Tk()
ventana.title("Variables de control")
nombre = tk.StringVar()

entrada = tk.Entry(ventana, textvariable=nombre, width=25)
entrada.pack()
espejo = tk.Label(ventana, textvariable=nombre, font=("Arial", 16), fg="#1a4d7a")
espejo.pack()
boton = tk.Button(ventana, text="Poner un ejemplo", command=poner_ejemplo)
boton.pack()

ventana.mainloop()