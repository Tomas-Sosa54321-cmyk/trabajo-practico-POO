class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def salario_anual(self):
        return self.salario * 13

    def __str__(self):
        return f"Nombre: {self.nombre}\nCargo: {self.cargo}\nSalario: {self.salario} Gs."

empleado1=Empleado("Marcio Jara", "Vendedor", 3700000)
empleado2=Empleado("Olga Gomez", "Cajera", 3000000)
empleado3=Empleado("Miguel Alvarez", "Encargado", 4500000)

print(empleado1)
print(f"Salario anual: {empleado1.salario_anual()} Gs.")

print("\n" + str(empleado2))
print(f"Salario anual: {empleado2.salario_anual()} Gs.")

print("\n" + str(empleado3))
print(f"Salario anual: {empleado3.salario_anual()} Gs.")