import tkinter as tk

def saludar():
    print("¡Hola! Me diste clic")


ventana = tk.Tk()

ventana.title("Dos botones")
ventana.geometry("300x110")
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()
tk.Button(
    ventana, 
    text="Salir", 
    command=ventana.destroy, 
    bg="blue", 
    fg='green'
).pack()

ventana.mainloop()