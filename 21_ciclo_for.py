
# Cuando no importa el valor inicial de i pero si la cantidad de vueltas
for i in range(5):
    print(f'Número de Vuelta: {i}')

print()
# Cuando requiero un valor inicial
for i in range(100, 111):
    print(f'Número de Vuelta: {i}')

print()
# Cuando si requiero que la i tenga saltos de mas de 1
for i in range(100, 111, 2):
    print(f'Número de Vuelta: {i}')

print()
# Cuando si requiero que la i tenga decrementos
for i in range(10, 0, -2):
    print(f'Número de Vuelta: {i}')