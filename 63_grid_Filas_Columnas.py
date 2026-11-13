import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("Formulario con grid")

etiqueta_nombre = tb.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entrada_nombre = tb.Entry(ventana, width=25)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

etiqueta_grupo = tb.Label(ventana, text="Grupo:")
etiqueta_grupo.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entrada_grupo = tb.Entry(ventana, width=8)
entrada_grupo.grid(row=1, column=1, sticky="w", padx=5, pady=5)

etiqueta_correo = tb.Label(ventana, text="Correo institucional:")
etiqueta_correo.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entrada_correo = tb.Entry(ventana, width=25)
entrada_correo.grid(row=2, column=1, padx=5, pady=5)

boton = tb.Button(ventana, text="Guardar", width=12)
boton.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()