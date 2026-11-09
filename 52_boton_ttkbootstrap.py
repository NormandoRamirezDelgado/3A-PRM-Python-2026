import ttkbootstrap as tb

def saludar():
    print("¡Hola! Me diste clic")

ventana = tb.Window()
ventana.title("Mi primer botón")
ventana.geometry("300x300")
boton = tb.Button(ventana, text="Saludar", command=saludar)
boton.pack()

guardar = tb.Button(ventana, text="Guardar", bootstyle="success")
guardar.pack()
cancelar = tb.Button(ventana, text="Cancelar", bootstyle="secondary-outline")
cancelar.pack()
borrar = tb.Button(ventana, text="Borrar todo", bootstyle="danger-outline")
borrar.pack()
salir = tb.Button(ventana, text="Salir", command=ventana.destroy, bootstyle="danger")
salir.pack()

ventana.mainloop()