import os

#------------------------------------------------------------------------------------------#

#MOSTRAR LISTA DE PRECIOS
def mostrar_lista():
    os.system("cls")
    print("-"*30)
    print("LISTA DE PRECIOS")
    print("-"*30)
    print("BEBIDAS")
    print("-"*30)

    for key,value in dic_bebidas.items():
        print(f" {key} - ${value}")

    print("-"*30)
    print("COMIDAS")
    print("-"*30)

    for key1, value1 in dic_comida.items():
        print(f" {key1} - ${value1}")

    print("-"*30)


#CARGAR BEBIDA
def cargar_bebida():
    while True:
        nombre = input("Ingrese nombre de la bebida (0 para salir): ")
        if nombre == '0':
            break
        else:
            try:
                precio = int(input(f"Ingrese el precio de {nombre}: "))
            except ValueError:
                print("precio mal ingresado")
            else:
                dic_bebidas[nombre] = precio
                
    return dic_bebidas


#CARGAR COMIDA
def cargar_comida():
    while True:
        nombre = input("Ingrese nombre de la comida (0 para salir): ")
        if nombre == '0':
            break
        else:
            try:
                precio = int(input(f"Ingrese el precio de {nombre}: "))
            except ValueError:
                print("precio mal ingresado")
            else:
                dic_comida[nombre] = precio
                
    return dic_comida


#MOSTRAR MENU
def menu():
    opcion = 0
    salir = True
    while salir:
        print("-"*30)
        print("Menu de Opciones")
        print("-"*30)
        print("1. Mostrar lista de precios")
        print("2. Ingresar Bebida")
        print("3. Ingresar Comida")
        print("0. Salir")
        print("-"*30)

        while True:
            try:
                opcion = int(input("Ingrese una Opcion: "))
            except:
                print("Opcion no valida")
            else:
                if opcion < 0 or opcion > 3:
                    print("Opcion debe ser un numero entre 0 y 3")
                else:
                    salir= False

                    break
    return opcion

#------------------------------------------------------------------------------------------#
#EJECUCION DEL PROGRAMA

dic_bebidas = {}
dic_comida = {}

while True:

    realizar = menu()

    if realizar == 0 :
        break
    elif realizar == 1:
        os.system("cls")
        mostrar_lista()
    elif realizar == 2:
        os.system("cls")
        cargar_bebida()
        print(dic_bebidas)
    elif realizar == 3:
        os.system("cls")
        cargar_comida()
        print(dic_comida)
    
