'''Un diccionario guarda pares clave: valor, como un diccionario real relaciona una palabra con su definición. Se escribe entre llaves { }. Accedes por la clave, no por posición.'''

alumno = {
    "nombre"    : "Ana",
    "edad"      : 16,
    "promedio"  : 9.2
}

print(alumno["nombre"])       # Ana (acceso por la clave)
alumno["edad"] = 17           # modificar un valor
alumno["grupo"] = "3°A-PRM"        # agregar un nuevo par clave-valor
print(alumno)