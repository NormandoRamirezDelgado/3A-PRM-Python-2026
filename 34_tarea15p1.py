'''
Hacer un programa que cree una Lista con 10 números enteros y realice lo siguiente:
Agregue un nuevo número
Imprimir el contenido de la posición que el usuario desee
Inserte un valor en la posición que el usuario desee
Imprima la lista
Eliminar la primera ocurrencia que el usuario desee
Extraer una sublista de 3 elementos de la posición 4 a la 6
Imprimir el tamaño de la lista
'''
numeros = []
for i in range(10):
    numeros.append(int(input('Introduce un valor entero:')))

posicion = int(input('Introduce la posición:'))
print(f'El contenido es: {numeros[posicion]}')

posicionInsertar = int(input('Introducir Posición:'))
numeroInsertar = int(input('Valor a Insertar:'))
numeros.insert(posicionInsertar, numeroInsertar)
print(numeros)

datoBorrar = int(input('Dato a Borrar:'))
numeros.remove(datoBorrar)
print(numeros)

sublista = numeros[4:7]
print(sublista)

print(len(numeros))





