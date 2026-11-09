import ttkbootstrap as tb

def saludar():
    mensaje.config(text="¡Hola! Me diste clic", bootstyle="success")
    boton.config(text="¡Listo!", bootstyle="success-outline")


ventana = tb.Window()
ventana.title("config()")
ventana.geometry("300x110")
mensaje = tb.Label(ventana, text="Esperando un clic…", font=("Arial", 13))
mensaje.pack()
boton = tb.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()