# Modificar, agregar y eliminar
frutas = ["manzana", "pera", "uva"]
print('\nLista Original')
print(frutas)

frutas[1] = "plátano"      # cambia el elemento en posición 1
print('\nModifica el valor de un elemento de la lista')
print(frutas)

frutas.append("naranja")   # agrega al final
print('\nAPPEND Agregar Elementos al Final de la Lista')
print(frutas)

frutas.insert(0, "kiwi")   # inserta "kiwi" en la posición 0
print('\nINSERT Inserta un valor en la pocisión deseada')
print(frutas)
frutas.remove("uva")  # elimina la primera ocurrencia de "uva"
print('\nREMOVE Elimina la primera Ocurrencia que encuentre de izquierda a derecha')
print(frutas)
ultimo = frutas.pop()      # elimina y devuelve el último elemento
print(f'\nEl elemento eliminado es: {ultimo}')
print(frutas, '\n')
