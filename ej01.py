class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre=nombre
        self.cedula=cedula
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}"


cliente1 = Cliente("Braulio Jara", "5789004", "0972966200")
cliente2 = Cliente("Brenda Rivas", "6036054", "0992764532")

print("Ficha del cliente")
print(cliente1)

print("\nFicha del Cliente")
print(cliente2)
