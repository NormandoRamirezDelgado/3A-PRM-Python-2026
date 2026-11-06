import tkinter as tk

def revisar():
    elegidos = []
    if robotica.get():
        elegidos.append("Robótica")
    if ajedrez.get():
        elegidos.append("Ajedrez")
    if musica.get():
        elegidos.append("Música")
    resultado.config(text=f"Elegiste {len(elegidos)}: {elegidos}")


ventana = tk.Tk()
ventana.title("Talleres")
ventana.geometry("340x170")

robotica = tk.BooleanVar()
ajedrez = tk.BooleanVar()
musica = tk.BooleanVar()


casilla_robotica = tk.Checkbutton(ventana, text="Robótica", variable=robotica)
casilla_robotica.pack()
casilla_ajedrez = tk.Checkbutton(ventana, text="Ajedrez", variable=ajedrez)
casilla_ajedrez.pack()
casilla_musica = tk.Checkbutton(ventana, text="Música", variable=musica)
casilla_musica.pack()

boton = tk.Button(ventana, text="¿Cuáles elegí?", command=revisar)
boton.pack()
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()