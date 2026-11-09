import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("Turno")
ventana.geometry("280x100")
turno = tb.StringVar()
turno.set("matutino")

opcion_matutino = tb.Radiobutton(ventana, text="Matutino", variable=turno, value="matutino", bootstyle="toolbutton")
opcion_matutino.pack()
opcion_vespertino = tb.Radiobutton(ventana, text="Vespertino", variable=turno, value="vespertino", bootstyle="info-toolbutton")
opcion_vespertino.pack()

ventana.mainloop()