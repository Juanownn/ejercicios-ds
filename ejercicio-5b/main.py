passwordCorrecta = "Hola123"

if __name__ == "__main__":
    intento = 0
    while intento < 3:
        password = str(input("Ingrese la contraseña: "))
        if password == passwordCorrecta:
            print("Contraseña correcta")
            break
        else: 
            intento += 1
            print(f"Contraseña incorrecta. Intentos restantes: {3 - intento}")

    if intento == 3:
        print("Intentos terminados. Cerrando...")