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

# Verificar si una clave existe y acceso seguro con .get()
alumno = {
    "nombre": "Ana",
    "edad": 16
}

# 1) Verificar con "in" antes de acceder
if "promedio" in alumno:
    print(alumno["promedio"])
else:
    print("No hay promedio registrado")

# 2) .get(clave, valor_por_defecto): devuelve el valor o el default si no existe
promedio = alumno.get("nombre", 0)   # no hay error aunque la clave no exista
if promedio == 0:
    print('Clave No Existe')
else:
    print(f'El Nombre es: {promedio}')
#print(promedio)  # 0

# Recorrer colecciones con for
alumno = {
    "nombre": "Ana", 
    "edad": 16, 
    "promedio": 9.2
}

print('\nRecorrido de un Diccionario')
for clave, valor in alumno.items():
    print(f"  {clave}   : {valor}")


# Lista de diccionarios — el formato de los registros reales
contactos = [
    {
        "nombre": "Ana",    
        "telefono": "555-1001", 
        "email": "ana@mail.com"
    },
    {
        "nombre": "Luis",  
        "telefono": "555-2002", 
        "email": "luis@mail.com"
    },
    {"nombre": "María",  "telefono": "555-3003", "email": "maria@mail.com"},
]

# Mostrar todos los contactos
print('\nMuestra Todos los Contactos del Diccionario de una Lista')
for i, contacto in enumerate(contactos):
    print(f"{i}. {contacto['nombre']} — Tel: {contacto['telefono']}")

# Buscar un contacto por nombre
print('\nBusca un Contacto por Nombre en cada Diccionario de la Lista')
buscar = "Luis"
for contacto in contactos:
    if contacto["nombre"] == buscar:
        print(f"Encontrado: {contacto['email']}")

# .keys() Devuelve una vista con todas las claves.
print(alumno.keys())    # dict_keys(['nombre', 'edad'])

# .values() Devuelve una vista con todos los valores.
print(alumno.values())  # dict_values(['Ana', 16])

# .update(otro) Agrega las claves de otro diccionario; si la clave ya existe, sobrescribe el valor.
alumno = {
    "nombre": "Ana", 
    "edad": 16
}
alumno.update(
    {
        "edad": 17, 
        "grupo": "3°A-PRM"
    }
)
print(alumno)  # {'nombre': 'Ana', 'edad': 17, 'grupo': '3°A'}

# .pop(clave, valor_defecto) Elimina la clave y devuelve su valor. Si no existe y no das valor por defecto, lanza KeyError
alumno = {
    "nombre": "Ana", 
    "edad": 16
}

edad = alumno.pop("edad")
print(edad)      # 16
print(alumno)    # {'nombre': 'Ana'}

alumno.pop("promedio", None)   # no existe, pero no da error

# .clear() Elimina todos los elementos.
alumno.clear()
print(alumno)   # {}


