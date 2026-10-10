def sumar_con_print(primero, segundo):
    return primero + segundo

def suma(uno, dos):
    return uno + dos

variable = 10
resultado = sumar_con_print(3, 4)
print(f'\nEl Resultado 1 es: {resultado}')

print(f'\nEl Resultado 2 es: {sumar_con_print(3, 4)}')

calcular = variable + sumar_con_print(3, 4)

print(f'\nResultado de Calcular: {calcular}\n')

print(f'La Suma de el argumento más la función es: {suma(20, sumar_con_print(3, 4))}\n')
