import ttkbootstrap as tb

def muestreoDatos():
    nombre = nombreEntry.get
    semestre = semestresT.get
    grupo = eleccionGrupo.get
    turno = turnoEleccion.get
    especialidad = eleccionEspecialidad.get
    salida.config(text=f"El nombre del Aulumno es: {nombre}, El semestre es: {semestre}, El grupo es:{grupo} , El turno es: {turno} , La especialidad es : {especialidad} ")

ventana = tb.Window()
ventana.geometry("800x600")
nombreAlumno = tb.Label(ventana , text="Ingresa tu nombre: ").pack
nombreEntry = tb.Entry(ventana)
nombreEntry.pack()
turnoAlumno = tb.Label(ventana, text="Seleccione el turno:").pack()
turnoEleccion=tb.StringVar(value="Matutino")
turnoMatutino = tb.Radiobutton(ventana , text="Matutino" , variable=turnoEleccion , value="Matutino")
turnoMatutino.pack()
turnoVespertino = tb.Radiobutton(ventana, text="vespertino", variable=turnoEleccion, value="Vespertino")
turnoVespertino.pack()
seleccionSemestre = tb.Label(ventana, text="Seleccione su semestre: ")
seleccionSemestre.pack()
semestres =["1er Semestre", "2do Semestre", "3er Semestre", "4to Semestre", "5to Semestre", "6to Semestre"]
semestresT = tb.Combobox(ventana, values=semestres)
semestresT.pack()
grupos = tb.Label(ventana, text="Seleccione su grupo: ").pack()
gruposT = ["A", "B", "C",]
eleccionGrupo = tb.Combobox(ventana, values=gruposT)
eleccionGrupo.pack()
especialidades= tb.Label(ventana, text="Seleccione su especiad").pack()
especialidadesA = ["Programacion","Recursos Humanos", "Puericultura", "Electricidad", "Contabilidad", "Inteligencia Artificial"]
eleccionEspecialidad = tb.Combobox(ventana, values=especialidadesA)
eleccionEspecialidad.pack()
boton = tb.Button(ventana, text="Mostrar Datos", command=muestreoDatos)
boton.pack()
salida = tb.Label(ventana, text="")
salida.pack()

boton_salir=tb.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack()

ventana.mainloop()