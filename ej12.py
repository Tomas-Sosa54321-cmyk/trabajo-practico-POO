class Linea:
    def __init__(self, cliente, gigabytes):
        self.cliente = cliente
        self.gigabytes = gigabytes
        self.consumidos = 0

    def registrar_consumo(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
        elif self.consumidos + cantidad > self.gigabytes:
            print("Aviso: el paquete de datos se agotó")
        else:
            self.consumidos += cantidad
            print(f"Consumo registrado: {cantidad} GB")

    def gigabytes_disponibles(self):
        return self.gigabytes - self.consumidos

    def __str__(self):
        return f"Cliente: {self.cliente}\nGB incluidos: {self.gigabytes}\nGB consumidos: {self.consumidos}\nGB disponibles: {self.gigabytes_disponibles()}"

linea=Linea("Braulio Jara", 12)

print(linea)

linea.registrar_consumo(3)
print(linea)

linea.registrar_consumo(4)
print(linea)

linea.registrar_consumo(5)
print(linea)