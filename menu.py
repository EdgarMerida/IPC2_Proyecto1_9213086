import os


def display():
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("\nSeleccionar un número de opción")
    print("\t1 - Cargar archivo")
    print("\t2 - Procesar archivo")
    print("\t3 - Escribir archivo salida")
    print("\t4 - Mostrar datos del estudiante")
    print("\t5 - Generar gráfica")
    print("\t6 - salir")

while True:

    display()

    # opción del usuario
    opcion = input("\nElige un número como opción >> ")

    if opcion == "1":
        print("")
        input("Has elegido la opción 1...\npulsa enter para continuar")
        #read.lineas_arch(read.leer_arch())
        
    elif opcion == "2":
        print("")
        input("Has elegido la opción 2...\npulsa enter para continuar")
    elif opcion == "3":
        print("")
        input("Has elegido la opción 3...\npulsa enter para continuar")
    elif opcion == "4":
        print("Edgar Estuardo Mérida Díaz")
        print("9213086")
        print("Introducción a la Programación y Computación 2 sección B")
        print("Ingeniería en Ciencias y Sistemas")
        print("4to. Semestre")
        input("\nHas elegido la opción 4...\npulsa enter para continuar >> ")
    elif opcion == "5":
        print("")
        input("Has elegido la opción 5...\npulsa enter para continuar")
    elif opcion == "6":
        break
    else:
        print("")
        input("Elegiste una opción incorrecta, ingresa un número de 1 a 6...\npulsa enter para continuar")

