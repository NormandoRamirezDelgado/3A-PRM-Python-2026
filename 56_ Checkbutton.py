import ttkbootstrap as tb

def revisar():
    elegidos = []
    if robotica.get():
        elegidos.append("Robótica")
    if ajedrez.get():
        elegidos.append("Ajedrez")
    if musica.get():
        elegidos.append("Música")
    resultado.config(text=f"Elegiste {len(elegidos)}: {elegidos}")


ventana = tb.Window()
ventana.title("Talleres")
ventana.geometry("340x170")
robotica = tb.BooleanVar()
ajedrez = tb.BooleanVar()
musica = tb.BooleanVar()

casilla_robotica = tb.Checkbutton(ventana, text="Robótica", variable=robotica)
casilla_robotica.pack()
casilla_ajedrez = tb.Checkbutton(ventana, text="Ajedrez", variable=ajedrez)
casilla_ajedrez.pack()
casilla_musica = tb.Checkbutton(ventana, text="Música", variable=musica)
casilla_musica.pack()
boton = tb.Button(ventana, text="¿Cuáles elegí?", command=revisar)
boton.pack()
resultado = tb.Label(ventana, text="")
resultado.pack()

ventana.mainloop()