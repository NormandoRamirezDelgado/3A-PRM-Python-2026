import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("pack: fill y expand")
ventana.geometry("360x220")

encabezado = tb.Label(ventana, text='fill="y"', bootstyle="inverse-primary")
encabezado.pack(fill='x')

contenido = tb.Label(ventana, text='fill="both", expand=True', bootstyle="inverse-secondary")
#contenido.pack(fill="both", expand=True)

pie = tb.Label(ventana, text="sin fill", bootstyle="inverse-warning")
#pie.pack()

ventana.mainloop()