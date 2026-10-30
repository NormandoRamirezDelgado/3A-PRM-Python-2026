import tkinter as tk

def revisar():
    anios = int(edad.get())
    resultado.config(text=f"En 2 años tendrás {anios + 2}. Tu clave tiene {len(clave.get())} letras.")


ventana = tk.Tk()
ventana.title("Edad y clave")
ventana.geometry("420x170")

etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.pack()
edad = tk.Entry(ventana, width=5)
edad.pack()
etiqueta_clave = tk.Label(ventana, text="Contraseña:")
etiqueta_clave.pack()
clave = tk.Entry(ventana, width=15, show="#")
clave.pack()
boton = tk.Button(ventana, text="Revisar", command=revisar)
boton.pack()
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()