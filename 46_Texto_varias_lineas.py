import tkinter as tk

def contar():
    texto = caja.get("1.0", "end-1c")
    con_salto = caja.get("1.0", tk.END)
    resultado.config(text=f"Caracteres: {len(texto)}   (leyendo hasta END: {len(con_salto)})")


def plantilla():
    caja.insert(tk.END, "\nLo que aprendí hoy: ")


ventana = tk.Tk()
ventana.title("Comentarios")
caja = tk.Text(
    ventana, 
    width=40, 
    height=10, 
    font=("Arial", 12)
)
caja.pack()

boton = tk.Button(ventana, text="Contar caracteres", command=contar)
boton.pack()
agregar = tk.Button(ventana, text="Agregar plantilla", command=plantilla)
agregar.pack()
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()