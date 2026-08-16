if __name__ == "__main__":
    while 1:
        print("Opciones:\n" \
                "1. Calcular suma de los primeros N numeros naturales. Ingrese N\n" \
                "2. Encontrar todos los divisibles por 3 en un rango ingresado\n" \
                "3. Salir")
        opt = int(input("Ingrese una opcion: "))

        match opt:
            case 1:
                num = int(input("Ingrese hasta que numero natural sumar: "))
                sum = 0
                for i in range(num+1):
                    sum += i
                print(f"La suma de los primeros {num} es : {sum}")
                break
            case 2:
                print("Ingrese el rango para los divisibles de 3")
                ini = int(input("Ingrese el inicio del rango: "))
                fin = int(input("Ingrese el final del rango: "))
                div3 = ini % 3
                match div3:
                    case 1:
                        ini += 2
                    case 2:
                        ini += 1
                print("Los divisibles son: ")
                for i in range(ini, fin + 1, 3):
                    print(i, end=" ")
                break
            case 3:
                print("Saliendo..")
                break
            case _:
                print("Opcion no existente. Ingrese una valida")
