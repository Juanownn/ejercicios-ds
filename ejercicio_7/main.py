def analizar_temperaturas(registros):
    temps = (max(registros), min(registros), sum(registros) / len(registros))
    return (temps)

if __name__ == "__main__":
    temperaturas = []
    seguir = True
    while seguir:
        temp = int(input("Ingresa una temperatura, 0 para salir: "))
        if temp != 0:
            temperaturas.append(temp)
        else:
            seguir = False
    if len(temperaturas) != 0:
        print(analizar_temperaturas(temperaturas))
