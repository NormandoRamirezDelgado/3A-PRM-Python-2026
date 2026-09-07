nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre, "— bienvenido al sistema.")
print(type(nombre))

print()
precio = float(input('¿Cuánto cuesta el producto? $'))
descuento = precio * 0.10
print(f'Descuento: ${descuento:.2f}')
print(f"Total: ${precio - descuento:.10f}")
print(f'Resultado: ${precio + descuento} ')
