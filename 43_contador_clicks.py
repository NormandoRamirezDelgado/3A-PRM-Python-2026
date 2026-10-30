import tkinter as tk

contador = 0

def sumar():
    global contador
    contador = contador + 1
    etiqueta.config(text=f"Clics: {contador}")

def restar():
    global contador
    contador = contador - 1
    etiqueta.config(text=f"Clics: {contador}")

def reiniciar():
    global contador
    contador = 0
    etiqueta.config(text=f"Clics: {contador}")

ventana = tk.Tk()
ventana.title("Contador")
ventana.geometry("360x210")

etiqueta = tk.Label(ventana, text="Clics: 0", font=("Arial", 18))
etiqueta.pack()
botonSumar = tk.Button(ventana, text="Sumar 1", command=sumar)
botonSumar.pack()
botonRestar = tk.Button(ventana, text="Restar -1", command=restar)
botonRestar.pack()
botonReiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar)
botonReiniciar.pack()

ventana.mainloop()