import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("Secciones")

titulo = tb.Label(ventana, text="Registro de alumnos", font=("Arial", 16, "bold"), bootstyle="primary")
titulo.pack(pady=8)

datos = tb.Labelframe(ventana, text="Datos del alumno", padding=10)
datos.pack(padx=10, fill="x")

etiqueta_nombre = tb.Label(datos, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, sticky="e")
entrada_nombre = tb.Entry(datos, width=28)
entrada_nombre.grid(row=0, column=1, padx=5, pady=3)
etiqueta_grupo = tb.Label(datos, text="Grupo:")
etiqueta_grupo.grid(row=1, column=0, sticky="e")
entrada_grupo = tb.Entry(datos, width=28)
entrada_grupo.grid(row=1, column=1, padx=5, pady=3)

botones = tb.Frame(ventana)
botones.pack(pady=10)

guardar = tb.Button(botones, text="Guardar", width=10)
guardar.pack(side="left", padx=5)
limpiar = tb.Button(botones, text="Limpiar", width=10)
limpiar.pack(side="left", padx=5)

ventana.mainloop()