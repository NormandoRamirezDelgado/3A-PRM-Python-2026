import ttkbootstrap as tb

ventana = tb.Window()
#ventana = tb.Window(themename="superhero")

#Imprimir los diferentes tipos de tema.
print(ventana.style.theme_names())

ventana.title("Control Escolar")
#ventana.geometry("400x250")
ventana.geometry("400x350+200+150")
ventana.resizable(False, False)

icono = tb.PhotoImage(file="icono.png")
ventana.iconphoto(True, icono)

saludo = tb.Label(ventana, text="¡Hola, CBTis 236!")
saludo.pack()

nombre = tb.Label(ventana, text="Nombre: Ana López")
nombre.pack()
grupo = tb.Label(ventana, text="Grupo: 3°A")
grupo.pack()
carrera = tb.Label(ventana, text="Carrera: Programación")
carrera.pack()

titulo = tb.Label(ventana, text="CBTis 236", bootstyle="inverse-primary", font=("Arial", 20, "bold"), padding=20)
titulo.pack()
subtitulo = tb.Label(ventana, text="Técnico en Programación", background="#56e9d8",font=("Calibri", 13, "italic"))
subtitulo.pack()
aviso = tb.Label(ventana, text="Inscripciones abiertas", bootstyle="danger", font=("Arial", 12), padding=10)
aviso.pack()

marca = tb.Label(ventana, text="Azul institucional", foreground="white", background="#56e9d8", font=("Arial", 24), padding=20)
marca.pack()

ventana.mainloop()
