#Programa 2: Ordenación de Arreglo Multidimensional
# Definimos la matriz multidimensional
matriz_2 = [
    [2, 4, 1],
    [5, 9, 7],
    [3, 6, 8]
]

# Mostramos la matriz desordenada
print("Matriz desordenada:")
for i in matriz_2:
    print(i)

# Ordenamos la segunda fila
# se ordena la fila con índice 1
matriz_2[1].sort()

# Mostramos la matriz con la segunda fila ordenada en orden ascendente
print("Matriz con la segunda fila ordenada en orden ascendente:")
for i in matriz_2:
    print(i)
