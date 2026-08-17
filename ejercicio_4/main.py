def conversorACelsius(temperatura):
    return((temperatura-32)/1.8)

def conversorAFarenheit(temperatura):
    return((temperatura * 1.8)+32)


if __name__ == "__main__":
    valTemp = int(input("Ingrese el valor de la temperatura: "))
    escala = input("Ingrese la escala. C para Celsius, F para Farenheit: ")

    match escala:
        case 'C':
            res = conversorAFarenheit(valTemp)
            escala = 'F'
        case 'F':
            res = conversorACelsius(valTemp)
            escala = 'C'
        case _:
            print("La escala ingresada es incorrecta")

    print(f"Su temperatura convertida es {res}°{escala}")

