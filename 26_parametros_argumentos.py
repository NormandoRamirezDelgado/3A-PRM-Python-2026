def saludar(nombre): # "nombre" es el parámetro
    print(f"¡Hola, {nombre}! Bienvenido.")

alumno = 'Luis'
saludar('Ana')                  # "Ana" es el argumento
saludar(alumno)                 # se reutiliza con otro argumento
saludar('Profe')                # misma función, resultado diferente