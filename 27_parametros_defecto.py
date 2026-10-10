def saludar_con_titulo(nombre, titulo="Alumno"):
    print(f"Bienvenido, {titulo} {nombre}")

saludar_con_titulo("Alumno")               # usa el default: Alumno García
saludar_con_titulo()               # usa el default: Alumno García
saludar_con_titulo("López", "Profesor")    # sobreescribe el default: Profesor López