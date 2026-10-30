import tkinter as tk

def saludar():
    mensaje.config(text="¡Hola! Me diste clic", fg="green")
    ventana.config(bg="lightgreen")

ventana = tk.Tk()
ventana.title("config()")
ventana.geometry("300x250")

mensaje = tk.Label(ventana, text="Esperando un clic…", font=("Arial", 13))
mensaje.pack()
boton = tk.Button(ventana, text="Saludar", command=saludar).pack()

ventana.mainloop()