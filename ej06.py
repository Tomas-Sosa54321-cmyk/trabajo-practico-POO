class Cuenta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def acreditar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se acreditaron {monto} Gs")
        else:
            print("El monto debe ser positivo")

    def consumir(self, monto):
        if monto <= 0:
            print("El monto debe ser positivo")
        elif monto > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto
            print(f"Compra realizada por {monto} Gs")

    def __str__(self):
        return f"Cliente: {self.cliente}\nSaldo: {self.saldo} Gs."


cuenta=Cuenta("Maria Paz Pettengill", 100000)

print(cuenta)

cuenta.acreditar(65000)
print(cuenta)

cuenta.consumir(34000)
print(cuenta)

cuenta.consumir(199000)
print(cuenta)