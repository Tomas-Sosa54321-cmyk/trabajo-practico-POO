class Habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado="Libre"

    def ocupar(self):
        if self.estado == "Ocupada":
            print("La habitación ya está ocupada")
        else:
            self.estado = "Ocupada"
            print("La habitación fue ocupada")

    def liberar(self):
        self.estado = "Libre"
        print("La habitación está libre")

    def calcular_estadia(self, noches):
        return self.tarifa * noches

    def __str__(self):
        return f"Habitación: {self.numero}\nTipo: {self.tipo}\nTarifa: {self.tarifa} Gs.\nEstado: {self.estado}"

habitacion = Habitacion(172, "Doble", 420000)

print(habitacion)

habitacion.ocupar()
print(habitacion)

costo = habitacion.calcular_estadia(3)
print(f"Costo de la estadía: {costo} Gs.")

habitacion.liberar()
print(habitacion)