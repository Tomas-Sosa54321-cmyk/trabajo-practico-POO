class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca=marca
        self.modelo=modelo
        self.año = año
        self.precio = precio

    def descripcion(self):
        return f"{self.marca} {self.modelo} {self.año} — {self.precio:,} Gs."

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.año} — {self.precio:,} Gs."
vehiculo1 = Vehiculo("Toyota", "Corolla", 2001, 25000000)
vehiculo2 = Vehiculo("Ford", "Bronco", 2021, 290000000)

print(vehiculo1.descripcion())
print(vehiculo2.descripcion())