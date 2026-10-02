# Números Primos e impares

for i in range(125, 201):
    contador = 0
    for j in range(2, i):
        if i % j == 0:
            contador = contador + 1
    if contador == 0:
        if i % 2 == 1:
            print(f'El número {i} es primo e impar')





print()
for i in range(125, 201):
    contador = True
    for j in range(2, i):
        if i % j == 0:
            contador = False
    if contador:
        if i % 2 == 1:
            print(f'El número {i} es primo e impar')