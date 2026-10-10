def estadisticas(uno, dos, tres):
    mayor = 0
    if uno > dos:
        if uno > tres:
            mayor = uno
        else:
            mayor = tres
    else:
        if dos > tres:
            mayor = dos
        else:
            mayor = tres 

    menor = 999999999999
    if uno < dos:
        if uno < tres:
            menor = uno
        else:
            menor = tres
    else:
        if dos < tres:
            menor = dos
        else:
            menor = tres 

    promedio = ( uno + dos + tres ) / 3
    return mayor, menor, promedio

valorMayor, valorMenor, valorPromedio = estadisticas(10, 6, 9)

print(f'El Mayor es: {valorMayor}')
print(f'El Menor es: {valorMenor}')
print(f'El Promedio es: {valorPromedio}')
