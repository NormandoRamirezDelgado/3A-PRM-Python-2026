'''
Hacer un programa que calcule el promedio de 5 calificaciones del alumno y de como resultado si el alumno aprobó o no el curso siendo la calificación mínima aprobatoria de 7.
'''
calificacionUno     = float(input('Calificación Uno: '))
calificacionDos     = float(input('Calificación Dos: '))
calificacionTres    = float(input('Calificación Tres: '))
calificacionCuatro  = float(input('Calificación Cuatro: '))
calificacionCinco   = float(input('Calificación Cinco: '))

promedio = ( calificacionUno + calificacionDos + calificacionTres + calificacionCuatro + calificacionCinco ) / 5

if promedio >= 7:
    print('Aprobó')
else:
    print('No Aprobó')
