import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("place")
ventana.geometry("360x200")

esquina = tb.Label(ventana, text="x=10, y=10",bootstyle="inverse-warning")
esquina.place(x=10, y=10)
otra = tb.Label(ventana, text="x=200, y=60", bootstyle="inverse-info")
otra.place(x=200, y=60)
centro = tb.Button(ventana, text="Centrado")
centro.place(relx=0.5, rely=0.75, anchor="center")

ventana.mainloop()