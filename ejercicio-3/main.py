

if __name__ == "__main__":
    costoPasaje = int(input("Ingrese el costo del pasaje: "))
    costoAlojamiento = int(input("Ingrese el precio por noche en el alojamiento: "))
    cantNoches = int(input("Cuantas noches se quedara: "))
    cantDinero = int(input("Dinero disponible: "))
    dineroRestante = cantDinero - (costoPasaje + (costoAlojamiento * cantNoches))
    if (cantDinero - (costoPasaje + (costoAlojamiento * cantNoches))) > 0:
        print(f"El dinero alcanza, sobra {dineroRestante}")
    else:
        print(f"El dinero no alcanza, falta {dineroRestante * -1}")
        