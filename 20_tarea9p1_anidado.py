alumno = 1
suma = 0

while alumno <= 5:

    contador = 1
    sumaCalificacion = 0
    while contador <= 5:
        calificacion = float(input('Calificación Uno:'))
        sumaCalificacion = sumaCalificacion + calificacion
        contador = contador + 1

    promedioAlumno = sumaCalificacion / 5
    suma = suma + promedioAlumno
    alumno = alumno + 1
promedioGrupal = suma / 5
print(f'El Promedio Grupal es de: {promedioGrupal:.2}')


