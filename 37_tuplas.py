'''Una tupla es como una lista, pero no se puede modificar una vez creada (es inmutable). Se escribe entre paréntesis ( ). Se usa para datos que no deben cambiar, como coordenadas o una fe'''
punto = (10, 20)  # coordenadas x, y
print(punto[0])   # 10 (se accede igual que en listas)
# punto[0] = 5  -> ERROR: las tuplas no se pueden modificar

# Se puede crear sin paréntesis
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

# Las tuplas también pueden ser anidadas
tupla = 1, 2, ('a', 'b', (10, 20, 30)), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][2][1]) #a

# Y también es posible convertir una lista en tupla haciendo uso de al función tuple().
lista = [1, 2, 3]
tupla = tuple(lista)
print(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

# Iterar una Tupla
tupla = [1, 2, 3]
for t in tupla:
    print(t) #1, 2, 3

#Desempaquetar una Tupla (Unpack)
numeros = (1, 2, 3)
x, y, z = numeros
print(x) #1
print(y) #2
print(z) #3

# Crear una Tupla con 1 solo elemento
tupla = (2,)
print(type(tupla)) #<class 'tuple'>
print(tupla)

# Métodos de Tuplas
'''count()
El método count() cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.'''
numeros = (1, 1, 1, 3, 1, 5)
print(numeros.count(1)) #4

'''index([,index])
El método index() busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado'''
numeros = (7, 7, 7, 3, 5)
print(numeros.index(3)) # Valor a buscar
print(numeros.index(3, 2)) # Valor buscar, posición inicial
print(numeros.index(3, 3, 5)) # Valor buscar, posición inicial y posición final - 1.