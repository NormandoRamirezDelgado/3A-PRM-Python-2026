# str → int: convertir texto que representa un número entero
edad_texto = "16"
edad = int(edad_texto)
print(edad + 1)          # 17 — ahora puedes hacer aritmética
print(edad_texto + 1)

# str → float: convertir texto que representa un decimal
precio_texto = "29.99"
precio = float(precio_texto)
print(precio * 1.16)     # 34.7884 — aplicar IVA

# int/float → str: convertir número a texto para pegarlo en un mensaje
calificacion = 9
mensaje = "Obtuviste " + str(calificacion) + " de 10"
print(mensaje)           # Obtuviste 9 de 10