import tkinter as tk

ventana = tk.Tk()

ventana.title("Control Escolar")
ventana.geometry("400x250")

icono = tk.PhotoImage(file="icono.png")
ventana.iconphoto(True, icono)

saludoUno = tk.Label(ventana, text="¡Hola, CBTis 236!")
saludoDos = tk.Label(ventana, text="¡Hola, CBTis 236 desde Tkinter!")

nombre = tk.Label(ventana, text="Nombre: Ana López").pack()
grupo = tk.Label(ventana, text="Grupo: 3°A").pack()
tk.Label(ventana, text="Carrera: Programación").pack()

saludoDos.pack()
saludoUno.pack()

titulo = tk.Label(ventana, text="CBTis 236", fg="white", bg="#1a4d7a", font=("Arial", 20, "bold"), width=20, pady=8)
titulo.pack()
subtitulo = tk.Label(ventana, text="Técnico en Programación", fg="red", font=("Arial 13 italic"))
subtitulo.pack()
aviso = tk.Label(ventana, text="Inscripciones abiertas", fg="darkred", bg="lightyellow", font=("Arial", 12), width=30, height=2).pack()


ventana.mainloop()
