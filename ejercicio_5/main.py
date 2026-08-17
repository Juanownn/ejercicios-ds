class MiExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.mensaje}"

if __name__ == "__main__":
    password = str(input("Ingrese su contraseña: "))

    if len(password) < 8:
        raise MiExcepcion("La contraseña debe ser de 8 o mas digitos")
    elif password.isdigit():
        raise MiExcepcion("La contraseña tiene que contener caracteres que no sean numeros unicamente")
    elif not any(c.islower() for c in password):
        raise MiExcepcion("La contraseña debe contener una minuscula")
    elif not any(c.isupper() for c in password):
        raise MiExcepcion("La contraseña debe contener una mayuscula")
    else:
        print(f"Contraseña correcta: {password}")