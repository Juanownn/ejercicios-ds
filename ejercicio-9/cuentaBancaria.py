class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            raise ValueError("Monto invalido")

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        else:
            self.saldo -= monto

    def mostrar_info(self):
        print(f"Mi titular es: {self.titular}")
        print(f"Mi saldo es: {self.saldo}")

#pruebas con instancias
cuenta1 = CuentaBancaria("Juano")
cuenta1.depositar(100)
cuenta1.mostrar_info()
cuenta1.retirar(50)
cuenta1.mostrar_info()
cuenta1.retirar(100)