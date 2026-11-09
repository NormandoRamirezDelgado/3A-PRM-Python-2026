import ttkbootstrap as tb

ventana = tb.Window()
ventana.title("Preferencias")
ventana.geometry("300x110")
avisos = tb.BooleanVar()
oscuro = tb.BooleanVar()

interruptor_avisos = tb.Checkbutton(ventana, text="Recibir avisos", variable=avisos, bootstyle="success-round-toggle")
interruptor_avisos.pack()
interruptor_oscuro = tb.Checkbutton(ventana, text="Modo oscuro", variable=oscuro, bootstyle="square-toggle")
interruptor_oscuro.pack()

ventana.mainloop()