import ttkbootstrap as tb

contador = 0

def sumar():
    global contador
    contador = contador + 1
    etiqueta.config(text=f"Clics: {contador}")

def restar():
    global contador
    contador = contador - 1
    etiqueta.config(text=f"Clics: {contador}")

def restablecer():
    global contador
    contador = 0
    etiqueta.config(text=f"Clics: {contador}")

ventana = tb.Window()

ventana.title("Contador")
ventana.geometry("260x210")
etiqueta = tb.Label(ventana, text="Clics: 0", font=("Arial", 28))
etiqueta.pack()
btnSuma = tb.Button(ventana, text="Sumar 1", command=sumar)
btnSuma.pack()
btnResta = tb.Button(ventana, text="Restar 1", command=restar)
btnResta.pack()
btnRestablece = tb.Button(ventana, text="Restablecer 0", command=restablecer)
btnRestablece.pack()

ventana.mainloop()