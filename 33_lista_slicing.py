numeros = [10, 20, 30, 40, 50]
print('\nLista Original')
print(numeros)

print('\nObtiene de la posición -5 - 4')
print(numeros[-1:4])    # [20, 30, 40] (posiciones 1, 2 y 3)

print('\nEspecifica solo la posición final por lo que imprime desde el inicio :3')
print(numeros[:3])     # [10, 20, 30] (desde el inicio hasta antes de 3)

print('\nEspecifica solo la posición inicial por lo que imprime desde el final 2:')
print(numeros[2:])     # [30, 40, 50] (desde posición 2 hasta el final)

rebanada = numeros[1:4]
print('\nExtraemos una sublista de una lista')
print(rebanada)
