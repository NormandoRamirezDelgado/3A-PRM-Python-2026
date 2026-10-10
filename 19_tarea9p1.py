'''
Hacer un programa que calcule el promedio de 50 alumnos de un grupo los cuales llevan 5 materias.

Se requiere mostrar el promedio obtenido por el grupo.
'''

alumno = 1
suma = 0

while alumno <= 5:
    calificacionUno = float(input('Calificación Uno:'))
    calificacionDos = float(input('Calificación Dos:'))
    calificacionTres = float(input('Calificación Tres:'))
    calificacionCuatro = float(input('Calificación Cuatro:'))
    calificacionCinco = float(input('Calificación Cinco:'))

    promedioAlumno = ( calificacionUno + calificacionDos + calificacionTres + calificacionCuatro + calificacionCinco ) / 5

    suma = suma + promedioAlumno

    alumno = alumno + 1

promedioGrupal = suma / 5
print(f'El Promedio Grupal es de: {promedioGrupal:.2}')
