'''
Hacer un programa que utilice el ciclo FOR que imprima la tabla de multiplicar que el usuario desee mostrando como resultado.
'''
numero = int(input('Número de la Tabla a crear: '))
for i in range(11):
    print(f'{numero} X {i} = {numero * i}')
