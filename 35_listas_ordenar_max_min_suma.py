calificaciones = [6, 10, 7, 9, 8]
print(calificaciones)
calificaciones.sort()   # ordena la lista EN SITIO (la modifica): [6, 7, 8, 9, 10]
ordenadas = sorted([6, 10, 7])  # devuelve nueva lista ordenada sin modificar la original
print(ordenadas)

print(min(calificaciones))            # 6
print(max(calificaciones))            # 10
print(sum(calificaciones))            # 40


