# Escritura de Archivo de Texto

# Abre o crea si no existe el archivo  en modo de escritura
# Si el archivo ya existe, será sobrescrito.
archivo = open("my_notes.txt", "w")

# se escriben tres líneas de notas  en el archivo
archivo.write("hola mundo\n")
archivo.write("aprendiendo a programar\n")
archivo.write("que viva el rock and roll\n")

# Cerrar el archivo para guardar los cambios
archivo.close()

# Lectura de Archivo de Texto

# Abre el archivo  en modo de lectura
archivo = open("my_notes.txt", "r")

# Lee el contenido del archivo línea por línea  y LO muestra en la consola
linea = archivo.readline()  # se lee la primera línea
while linea:  # Mientras la línea no esté vacía
    print(linea.strip())  # se muestra la línea sin los saltos de línea adicionales
    linea = archivo.readline()  # se lee la siguiente línea

# se cierra el archivo después de la lectura
archivo.close()

# Verificar si el archivo ha sido cerrado
print("\nArchivo cerrado:", archivo.closed)
