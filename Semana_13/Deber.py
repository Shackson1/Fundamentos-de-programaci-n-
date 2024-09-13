

#creación de la matriz tridimencional la cual contiene ciudades, semanas y días.
matriz=[
    #Quito
    [
        #Semana 1
        [
            #lunes
            {"dia": "lunes", "temperatura": 22},
            #mastes
            {"dia":"martes", "temperatura": 24},
            #miercoles
            {"dia":"miercoles", "temperatura": 25},
            #jueves
            {"dia":"jueves", "temperatura": 27},
            #viernes
            {"dia":"viernes", "temperatura": 23},
            #sabado
            {"dia":"sabado", "temperatura": 21},
            #domingo
            {"dia":"domingo", "temperatura": 24}

        ],
        #semana 2
        [

            # lunes
            {"dia":"lunes", "temperatura": 24},
            # mastes
            {"dia":"marte", "temperatura": 22},
            # miercoles
            {"dia":"miercoles", "temperatura": 20},
            # jueves
            {"dia":"jueves", "temperatura": 24},
            # viernes
            {"dia":"viernes", "temperatura": 23},
            # sabado
            {"dia":"sabado", "temperatura": 21},
            # domingo
            {"dia":"domingo", "temperatura": 26}

        ],
        #semana 3
        [

            # lunes
            {"dia":"lunes", "temperatura": 22},
            # mastes
            {"dia":"martes", "temperatura": 21},
            # miercoles
            {"dia":"miercoles", "temperatura": 20},
            # jueves
            {"dia":"jiueves", "temperatura": 19},
            # viernes
            {"dia":"viernes", "temperatura": 21},
            # sabado
            {"dia":"sabado", "temperatura": 23},
            # domingo
            {"dia":"domingo", "temperatura": 24}

        ],
        #semana 4
        [

            # lunes
            {"dia":"lunes", "temperatura": 24},
            # mastes
            {"dia":"martes", "temperatura": 23},
            # miercoles
            {"dia":"miercoles", "temperatura": 25},
            # jueves
            {"dia":"jueves", "temperatura": 20},
            # viernes
            {"dia":"viernes", "temperatura": 19},
            # sabado
            {"dia":"sabado", "temperatura": 23},
            # domingo
            {"dia":"domingo", "temperatura": 22}

        ]
    ],
    #Puyo
    [
        #semana 1
        [

            # lunes
            {"dia":"lunes", "temperatura": 24},
            # mastes
            {"dia":"martes", "temperatura": 21},
            # miercoles
            {"dia":"miercoles", "temperatura": 25},
            # jueves
            {"dia":"jueves", "temperatura": 23},
            # viernes
            {"dia":"viernes", "temperatura": 23},
            # sabado
            {"dia":"sabado", "temperatura": 26},
            # domingo
            {"dia":"domingo", "temperatura": 22}

        ],
        #semana 2
        [

            # lunes
            {"dia":"lunes", "temperatura": 29},
            # mastes
            {"dia":"martes", "temperatura": 28},
            # miercoles
            {"dia":"miercoles", "temperatura": 27},
            # jueves
            {"dia":"jueves", "temperatura": 32},
            # viernes
            {"dia":"viernes", "temperatura": 29},
            #sabado
            {"dia":"sabado", "temperatura": 31},
            # domingo
            {"dia":"domingo", "temperatura": 30}

        ],
        #semana 3
        [

            # lunes
            {"dia":"lunes", "temperatura": 29},
            # mastes
            {"dia":"martes", "temperatura": 32},
            # miercoles
            {"dia":"miercoles", "temperatura": 33},
            # jueves
            {"dia":"jueves", "temperatura": 35},
            # viernes
            {"dia":"viernes", "temperatura": 31},
            # sabado
            {"dia":"sabado", "temperatura": 36},
            # domingo
            {"dia":"domingo", "temperatura": 37}

        ],
        #semana4
        [

            # lunes
            {"dia":"lunes", "temperatura": 32},
            # mastes
            {"dia":"martes", "temperatura": 31},
            # miercoles
            {"dia":"miercoles", "temperatura": 36},
            # jueves
            {"dia":"jueves", "temperatura": 36},
            # viernes
            {"dia":"viernes", "temperatura": 32},
            # sabado
            {"dia":"sabado", "temperatura": 33},
            # domingo
            {"dia":"domingo", "temperatura": 38}

        ]
    ],
    #Tena
    [
        #semana 1
        [

            # lunes
            {"dia":"lunes", "temperatura": 25},
            # mastes
            {"dia":"martes", "temperatura": 25},
            # miercoles
            {"dia":"miercoles", "temperatura": 28},
            # jueves
            {"dia":"jueves", "temperatura": 26},
            # viernes
            {"dia":"viernes", "temperatura": 34},
            # sabado
            {"dia":"sabado", "temperatura": 29},
            # domingo
            {"dia":"domingo", "temperatura": 25}

        ],
        #semana 2
        [

            # lunes
            {"dia":"lunes", "temperatura": 29},
            # mastes
            {"dia":"martes", "temperatura": 32},
            # miercoles
            {"dia":"miercoles", "temperatura": 29},
            # jueves
            {"dia":"jueves", "temperatura": 28},
            # viernes
            {"dia":"viernes", "temperatura": 26},
            # sabado
            {"dia":"sabado", "temperatura": 21},
            # domingo
            {"dia":"domingo", "temperatura": 34}

        ],
        #semana 3
        [

            # lunes
            {"dia":"lunes", "temperatura": 28},
            # mastes
            {"dia":"martes", "temperatura": 28},
            # miercoles
            {"dia":"miercoles", "temperatura": 26},
            # jueves
            {"dia":"jueves", "temperatura": 27},
            # viernes
            {"dia":"viernes", "temperatura": 23},
            # sabado
            {"dia":"sabado", "temperatura": 21},
            # domingo
            {"dia":"domingo", "temperatura": 20}

        ],
        #semana 4
        [

            # lunes
            {"dia":"lunes", "temperatura": 25},
            # mastes
            {"dia":"martes", "temperatura": 23},
            # miercoles
            {"dia":"miercoles", "temperatura": 21},
            # jueves
            {"dia":"jueves", "temperatura": 20},
            # viernes
            {"dia":"viernes", "temperatura": 28},
            # sabado
            {"dia":"sabado", "temperatura": 24},
            # domingo
            {"dia":"domingo", "temperatura": 26}

        ]
    ]
]


#definicion de la función y sus parámetros
def temp_promedio(matriz,ciudad,semana): #la función recibe como parámetros la matriz creada anteriormente, la ciudad y la semana de las que se extraerán los datos.

    #se inicia una variable en cero
    suma_temp_ciudad_sem = 0

    #búcle que itera sobre los parametros de la función, en estecaso la matriz.
    for k in range(len(matriz[ciudad][semana])):  # Recorre la ciudad y los días de la semana que se recibieron como parámetros y extrae la temperatura.
        #se suma el valor de la temperatura a la variable iniciada en cero anteriormente.
        suma_temp_ciudad_sem += matriz[ciudad][semana][k]["temperatura"]
    #se inicia una variable en cero para calcular el promedio de temperaturas
    promedio_temp_ciudad_sem = 0
    #se calcula el promedio de la temperatura
    promedio_temp_ciudad_sem = suma_temp_ciudad_sem / len(matriz[ciudad][semana])
    return promedio_temp_ciudad_sem

#se le da la opción al usuario de elegir de que ciudad y semana calcular el promedio.
print("seleccione una ciudad")
ciudad=int(input("0:Quito, 1: Puyo, 2: Tena"))
print("seleccione una semana")
elige_semana=int(input("1:semana 1, 2: semana 2, 3:semana 3, 4:semana 4"))
semana = elige_semana-1#se le resta 1 al valor ingresado por el usuario para que coincida con el indice de la semana de la que desee calcular el promedio

#llama a la función
resultado=temp_promedio(matriz,ciudad,semana)
#imprime el resultado.
print ("el promedio de temperatura para la ciudad y semana seleccionadas  es de:",resultado,"℃")