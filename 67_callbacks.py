import ttkbootstrap as tb

def calcular_total(precio, cantidad):
    total = precio * cantidad
    if total > 100:
        total = total * 0.9
    return round(total, 2)

def al_calcular():
    precio = float(entrada_precio.get())
    cantidad = int(entrada_cantidad.get())
    total = calcular_total(precio, cantidad)
    resultado.config(text=f"Total a pagar: ${total}")


ventana = tb.Window()
ventana.title("Cooperativa")

etiqueta_precio = tb.Label(ventana, text="Precio:")
etiqueta_precio.grid(row=0, column=0, sticky="e", padx=5, pady=4)
entrada_precio = tb.Entry(ventana, width=10)
entrada_precio.grid(row=0, column=1, padx=5, pady=4)
etiqueta_cantidad = tb.Label(ventana, text="Cantidad:")
etiqueta_cantidad.grid(row=1, column=0, sticky="e", padx=5, pady=4)
entrada_cantidad = tb.Entry(ventana, width=10)
entrada_cantidad.grid(row=1, column=1, padx=5, pady=4)
boton = tb.Button(ventana, text="Calcular", command=al_calcular)
boton.grid(row=2, column=0, columnspan=2, pady=6)
resultado = tb.Label(ventana, text="", font=("Arial", 13, "bold"))
resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=6)

ventana.mainloop()