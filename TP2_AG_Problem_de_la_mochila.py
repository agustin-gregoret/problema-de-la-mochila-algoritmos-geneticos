import os                      #interactua con el SO permitiendo limpiar la pantalla y pausar la ejecución del programa.
from itertools import product  #product es una función que genera el producto cartesiano de los objetos


objetos = [         #objeto definido como una lista de vectores/tuplas, 
    (1,150,20),     #donde cada tupla representa un objeto con su id, volumen y valor.
    (2,325,40),
    (3,600,50),
    (4,805,36),
    (5,430,25),
    (6,1200,64),
    (7,770,54),
    (8,60,18),
    (9,930,46),
    (10,353,28)
]

def limpiar_pantalla(): #lo usamos para limpiar la pantalla de la consola
    os.system("cls" if os.name == "nt" else "clear")

def pausa(): #lo usamos para pausar la ejecución del programa hasta que el usuario presione ENTER
    input("\nPresione ENTER para continuar...")



def mostrar_objetos():
    print("\nOBJETOS DISPONIBLES")
    print("-" * 45)
    print("Obj\tVolumen\t\tValor")
    print("-" * 45)

    for obj in objetos:         #Recorremos la lista de objetos y mostramos sus detalles
        print(f"{obj[0]}\t{obj[1]}\t\t${obj[2]}")

    pausa()





def busqueda_exhaustiva():
    limpiar_pantalla()

    print("===================================")
    print("    BUSQUEDA EXHAUSTIVA")
    print("===================================")

    
    capacidad = int(input("Capacidad de la mochila (cm3): "))

    mejor_valor, mejor_combinacion, volumen_utilizado = exhaustiva(capacidad, objetos) 
    #lo que realiza es llamar a la función exhaustiva con la capacidad y los objetos, y devuelve el mejor valor,
    #la mejor combinación de objetos y el volumen utilizado.


    print(f"\nCapacidad elegida: {capacidad} cm3")
    print(f"Mejor combinación: {mejor_combinacion}")
    print(f"Volumen utilizado: {volumen_utilizado} cm3")
    print(f"Mejor valor: ${mejor_valor}")

    pausa() 



#sirve para encontrar la mejor combinación de objetos que maximice el valor sin exceder la capacidad de la mochila.
def exhaustiva(capacidad_mochila_ingresada, objetos): 
    
    #P1
    mejor_valor = 0  
    mejor_combinacion = [] 
    mejor_volumen = 0 

    #P1(a)
    combinaciones = product([0, 1], repeat=len(objetos))
     #combinaciones se genera a medida que se itera sobre cada combinacion (de objetos).
    

    #P2
    for combinacion in combinaciones:  

        volumen_total = 0       #acumular el volumen total de la combinación ACTUAL.
        valor_total = 0         #acumular el valor   total de la combinación ACTUAL.
        combinacion_actual = [] #lista para almacenar los IDs de los objetos seleccionados en la combinación ACTUAL.
        
        #--P3--
        for j in range(len(objetos)):
            
            #P4
            if combinacion[j] == 1:
                volumen_total += objetos[j][1]  
                valor_total += objetos[j][2]
                combinacion_actual.append(objetos[j][0]) 

        #P5
        if volumen_total <= capacidad_mochila_ingresada and valor_total > mejor_valor: 
            mejor_valor = valor_total
            mejor_combinacion = combinacion_actual
            mejor_volumen = volumen_total
    return mejor_valor, mejor_combinacion, mejor_volumen #P6




def algoritmo_greedy(): #interfaz para eleccion de criterio de ordenamiento y ejecución del algoritmo greedy
    limpiar_pantalla()

    print("===================================")
    print("       ALGORITMO GREEDY")
    print("===================================")

    #P1
    capacidad = int(input("Capacidad de la mochila (cm3): "))

    #Submenú
    print("\nSeleccione el criterio:")
    print("1) Mejor Valor")
    print("2) Mejor Volumen")
    print("3) Mejor relación Valor/Volumen")

    #eleccion del criterio de ordenamiento para el algoritmo greedy
    opcion = input("\nOpción: ")


    # Validamos que la opción ingresada sea correcta (1, 2 o 3)
    if opcion in ["1", "2", "3"]:

        combinacion, volumen, valor = greedy(capacidad, objetos, opcion)
            #Invoca la función greedy pasandole por parametro los tres datos. 
             
        #Devuelve la combinación de objetos seleccionados, el volumen total utilizado y el valor total obtenido.
        print("\n--- RESULTADO ---")
        print(f"Objetos seleccionados: {combinacion}")
        print(f"Volumen utilizado: {volumen} cm3")
        print(f"Valor total: ${valor}")

    else:
        print("\nOpción inválida.")

    pausa()




def greedy(capacidad, objetos_cualquiera, opcion): 
#Es para seleccionar objetos de la lista segun un criterio de ordenamiento 
# sin exceder la capacidad de la mochila 

    #P1
    if opcion == "1":
        # Opción 1: Mayor Valor primero (objeto[2] es el precio/valor)
        objetos_ordenados = sorted(objetos_cualquiera, key=lambda obj: obj[2], reverse=True)

    elif opcion == "2":
        # Opción 2: Menor Volumen primero (objeto[1] es el volumen)
        # Nota: conviene priorizar los más chicos para que entren      #aquí reverse=False (de menor a mayor volumen).
        objetos_ordenados = sorted(objetos_cualquiera, key=lambda obj: obj[1], reverse=False)

    else:
        # Opción 3: Mejor relación Valor/Volumen (objeto[2] / objeto[1])
        objetos_ordenados = sorted(objetos_cualquiera, key=lambda obj: obj[2] / obj[1], reverse=True)
                                                       #valor en proporcion a su peso
                                                       
    #P2
    combinacion = []
    volumen = 0
    valor = 0


    #P3
    for objeto in objetos_ordenados: #Recorremos la lista de objetos ordenados según el criterio elegido por el usuario.
        numero = objeto[0]          #id
        volumen_objeto = objeto[1]  #volumen 
        valor_objeto = objeto[2]    #valor

        if volumen + volumen_objeto <= capacidad: #si el vol actual + el vol del objeto es <= a la capacidad de la mochila,
            combinacion.append(numero)            #entonces se agrega el objeto a la combinacion.
            volumen += volumen_objeto             #se actualiza el volumen total + el volumen del objeto agregado.
            valor += valor_objeto                 #se actualiza el valor total + el valor del objeto agregado.

    return combinacion, volumen, valor




def comparar():
    
    #P1
    # Creamos los nuevos objetos para la comparacion de los algoritmos --> ( id, peso(en gramos), valor )
    objetos2 = [   
        (1, 1800, 72),   
        (2, 600, 36),
        (3, 1200, 60)
    ]

    limpiar_pantalla()

    print("===================================")
    print(" COMPARACIÓN DE ALGORITMOS")
    print("===================================")

    #P2
    while True: #es un bucle para la validacion de la opcion ingresada por el usuario, si no es valida, se le pedira que ingrese nuevamente.

        opc = input("\nSeleccione el criterio para Greedy \n1: Mejor Valor, \n2: Mejor Peso, \n3: Mejor relación Valor/Peso\nOpción: ")
    
        # Verificamos si la opción ingresada está dentro de las válidas
        if opc in ["1", "2", "3"]:
            break                   # Rompe el bucle while y continúa con el programa
        else:  
            print("Opción inválida. Por favor, elija 1, 2 o 3.")


    print("\n>> Ejecutando ambos algoritmos para una capacidad de 3000 grs.")
    print(">> Comparando Grado de Optimización...")

    #P3
    # Ejecución del Algoritmo Greedy con la opción elegida por el usuario
    combinacion, peso_greedy, valor = greedy(3000, objetos2, opc) #Devuelve la combinación de objetos seleccionados, el peso total utilizado y el valor total obtenido.


    #criterios es un diccionario que relaciona las opciones del menú con sus descripciones.
    criterios = {"1": "Mejor Valor", "2": "Mejor Peso", "3": "Relación Valor/Peso"} 
    print(f"\n--- RESULTADO GREEDY ({criterios[opc]}) ---")

    print(f"Objetos seleccionados: {combinacion}")
    print(f"Peso utilizado: {peso_greedy} grs.")
    print(f"Valor total: ${valor}")


    #P4
    print("\n--- RESULTADO EXHAUSTIVA ---")
    mejor_valor, mejor_combinacion, peso_exh = exhaustiva(3000, objetos2)
        
    print(f"Objetos seleccionados: {mejor_combinacion}")
    print(f"Peso utilizado: {peso_exh} grs.")
    print(f"Mejor valor obtenido: ${mejor_valor}")
    
    pausa()


def menu(): #esta función es la que muestra el menú principal y permite al usuario seleccionar las opciones

    while True:

        limpiar_pantalla()

        print("=" * 45)
        print("     TRABAJO PRÁCTICO N°2")
        print("      PROBLEMA DE LA MOCHILA")
        print("=" * 45)

        print("\n1) Mostrar objetos")
        print("2) Búsqueda Exhaustiva")
        print("3) Algoritmo Greedy")
        print("4) Comparar métodos")
        print("0) Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_objetos()

        elif opcion == "2":
            busqueda_exhaustiva()

        elif opcion == "3":
            algoritmo_greedy()

        elif opcion == "4":
            comparar()

        elif opcion == "0":
            print("\nHasta luego.")
            break

        else:
            print("\nOpción inválida.")
            pausa()


menu()