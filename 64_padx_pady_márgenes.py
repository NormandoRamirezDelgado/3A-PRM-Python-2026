import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("Barra de botones")
ventana.geometry("360x80")

nuevo1 = tb.Button(ventana, text="Arriba", width=8)
nuevo1.pack(side="top", pady=50)
nuevo = tb.Button(ventana, text="Nuevo", width=8)
nuevo.pack(side="left", padx=10)
guardar = tb.Button(ventana, text="Guardar", width=8)
guardar.pack(side="left", padx=10)
salir = tb.Button(ventana, text="Salir", width=8, command=ventana.destroy)
salir.pack(side="left", padx=10)

ventana.mainloop()