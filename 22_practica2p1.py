suma_Promedios = 0.0
for i in range(5):  # Para 10 Alumnos
    suma = 0.0
    for j in range(3):  # Para 8 Calificaciones por Almno
        calificacion = float(input('Calificación: '))
        suma = suma + calificacion
    promedio = suma / 3
    sumaPromedios = sumaPromedios + promedio
promedioGrupal = sumaPromedios / 5
print(f'El Promedio Grupal es de: {promedioGrupal}')

