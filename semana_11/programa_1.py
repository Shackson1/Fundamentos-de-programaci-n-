# Definimos la matriz 3x3
matriz_1 = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

# Solicitamos al usuario que ingrese el valor a buscar
valor_buscado = int(input("Ingrese el valor entre 1 y 17 que desea encontrar : "))

# Función que busca un valor en la matriz y devuelve su índice
def buscar_valor(matriz_1, valor_buscado):
    # Itera sobre cada una de las filas de la matriz
    for i in range(len(matriz_1)):
        # Itera sobre cada uno de los elementos dentro de la fila
        for j in range(len(matriz_1[i])):
            # Comprueba si el valor buscado se encuentra en la posición actual de la matriz
            if matriz_1[i][j] == valor_buscado:
                # Devuelve los índices de fila y columna
                return (i, j)
    # Si no se encuentra el valor, devuelve None
    return None
# Llamada a la función
resultado = buscar_valor(matriz_1, valor_buscado)

# Condicional que muestra el resultado si se encontró el valor
if resultado:
    print(f"El valor {valor_buscado} se encuentra en la matriz y su  posición es:{resultado}.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz.")
