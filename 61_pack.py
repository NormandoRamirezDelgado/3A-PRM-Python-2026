import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("pack: side")
ventana.geometry("360x200")

arribaUno = tb.Label(ventana, text="TOP1", bootstyle="inverse-warning", width=10)
arribaUno.pack()
arribaDos = tb.Label(ventana, text="TOP2", bootstyle="inverse-warning", width=10)
arribaDos.pack()
abajoUno = tb.Label(ventana, text="BOTTOM1", bootstyle="inverse-success", width=10)
abajoUno.pack(side="bottom")
abajoDos = tb.Label(ventana, text="BOTTOM2", bootstyle="inverse-success", width=10)
abajoDos.pack(side="bottom")
izquierda = tb.Label(ventana, text="LEFT", bootstyle="inverse-info", width=10)
izquierda.pack(side="left")
derecha = tb.Label(ventana, text="RIGHT1", bootstyle="inverse-danger", width=10)
derecha.pack(side="right")
derechaDos = tb.Label(ventana, text="RIGHT2", bootstyle="inverse-danger", width=10)
derechaDos.pack(side="right")

ventana.mainloop()