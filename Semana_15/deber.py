#creación de la lista que contiene los datos personales de una persona
informacion_personal = {"nombre":"Rambo", "edad":57, "ciudad":"Quito"}

def accederdicc (nombredicc,clave):
    acceder=nombredicc[clave]
    return acceder
#función que modifica un valor
def modificarvalor (nombredicc,clave,valor_modificado):
    modificado= nombredicc[clave]= valor_modificado
    return modificado

#función que agrega un valor
def agregarvalor (nombredicc,clave,valor):
    valor_agregado=nombredicc[clave]=valor
    return valor_agregado

#función que verifica la existencia de un valor
def verificarexistecia (valor_verificar,nombredicc):
    verificar=valor_verificar in nombredicc
    return verificar

#función que elimina un valor
def eliminarvalor (nombredicc,clave):
    del(nombredicc[clave])

#se muestran los datos al usuario
print("tus datos son:",informacion_personal)

#bucle que mantiene funcionando el programa segun las opciones que elija el usuario
while True:

    #se le presentan las opciones al usuario
    opcion=int(input("1:escriba 1 para modificar información,"
                     "2:escriba 2 para agregar información,"
                     "3:escriba 3 para verificar existencia de un valor,"
                     "4:escriba 4 para eliminar información,"
                     "5:escriba 5 para cerrar el programa"))
    #estructura condicionl que ejecuta un bloque de codigo segun la opción ingresada por el usuario
    match opcion:
        # en caso que el usuario escriba la opción 1
        case 1:
            #se le pide al usuario que ingrese la clave de la información que desea modificar
            clave1 = input("ingrese la clave del valor que desea modificar")
            #se le pide al usuario que ingrese la nueva información
            nuevo_valor = input("ingrese el valor modificado")
            #se llama a la función que modifica un valor y se ingresa como argumentos la clave y el nuevo valor ingresados por el usuario
            valor_nuevo = modificarvalor(informacion_personal, clave1, nuevo_valor)
            #se muestra la clave modificada y el nuevo dccionario con la infromación actualizada
            print(f"se ha modificado {clave1}:", informacion_personal)
        #en caso de que el usuario ingrese la opción 2
        case 2:
            #se le pide al usuario la nueva clave
            nuevaclave = input("ingrese la nueva clave")
            #se le pide al usuario el valor para la nueva clave
            nuevovalor = input("ingrese el valor para la clave")
            #se llama a la función que agrega un valor y se ingresa como argumentos la nueva clave y el nuevo valor ingresados por el usuario
            agregarvalor(informacion_personal,nuevaclave,nuevovalor)
            #se imprime el nuevo diccionario con la información  nueva
            print(f"se agrego {nuevaclave} a la información personal:",informacion_personal)
        #en caso el usuario ingrese la opción 3
        case 3:
            #se le pide al usuario que ingrese la infrmación para verificar
            valoraverificar=input("ingrese la  información a verificar")
            #se llama a la función que verifica la existencia de información y se ingresa el valor a verificar ingresado por el usuario
            verificacion=verificarexistecia(valoraverificar,informacion_personal)
            #si la información no existe
            if verificacion==False:
                #se muestra al usuario que la información no existe
                print(valoraverificar,"no se encuentra en la información personal")
                #se le pregunta al usuario si desea agregar la información o desea continuar
                pregunta=int(input("1:escriba 1 si desea agregarlo,2:escriba 2 para continuar"))
                #si el usuario escribe  opción 1
                if pregunta == 1:
                    #se le pide al usuario que ingrese el valor de la información que consultó
                    nueva_valor=input(f"ingrese su {valoraverificar}: ")
                    #se llama a la función que agrega un valor y se ingresa como argumentos el diccionaio,el valor que verificó el usuario y el nuevo valor ingresado por el usuario
                    agregarvalor(informacion_personal,valoraverificar,nueva_valor)
                    #se imprime el diccionario con la información agregada
                    print(f"se agrego {valoraverificar} a la información personal:", informacion_personal)
            #si la información existe se la muestra al usuario
            else:
                print(f"su {valoraverificar} es:",informacion_personal[valoraverificar])
        #si el usuario escribe la opción 4
        case 4:
            #se le muestra la información al usuario
            print(informacion_personal)
            #se le pode al usuario que ingrese la clave del valor que desea eliminar
            valorparaeliminar= input("escriba la clave del valor que desea eliminar")
            #se llama a la función que elimina un valor y se ingresa como argumento el diccionario y la clave que ingresó el usuario para eliminar
            valoreliminado=eliminarvalor(informacion_personal,valorparaeliminar)
            #se muestra el diccionario sin la información eliminada
            print(f"{valorparaeliminar} se eliminó de la información personal:",informacion_personal)
        #si el usuario escribe la opción 5 se cierra el prgrama
        case 5:
            print("gracias por utilizar el programs")
            break







