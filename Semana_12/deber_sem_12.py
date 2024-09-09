

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

ciudades = ["Quito", "Puyo", "Tena"]

# Bucle para recorrer cada ciudad
for i, ciudad in enumerate(matriz):
    print(f"\nPromedio de temperaturas para {ciudades[i]}:")

    # Bucle para recorrer cada semana dentro de la ciudad
    for j, semana in enumerate(ciudad):
        suma_temperaturas = 0

        # Bucle para recorrer cada día de la semana y sumar las temperaturas
        for dia in semana:
            suma_temperaturas += dia["temperatura"]

        # Calcular el promedio
        promedio = suma_temperaturas / len(semana)

        # Mostrar el promedio de la semana
        print(f"  Semana {j + 1}: {promedio:.2f} °C")
