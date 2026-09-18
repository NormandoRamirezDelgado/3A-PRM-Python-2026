contador = 1

while contador <= 5:
    print("Vuelta número", contador)
    contador += 1      # ¡clave! sin esta línea, contador nunca cambia y el ciclo no termina
print("Terminó el ciclo")