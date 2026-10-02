class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio = precio
        self.stock = stock

    def valor_total(self):
        return self.precio * self.stock

    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio} Gs.\nStock: {self.stock}"


producto1 = Producto("Galletita", 3200, 15)
producto2 = Producto("Jabón", 4500, 21)
producto3 = Producto("Detergente", 9450, 17)

print(producto1)
print(f"Valor total en stock: {producto1.valor_total()} Gs.")

print("\n" + str(producto2))
print(f"Valor total en stock: {producto2.valor_total()} Gs.")

print("\n" + str(producto3))
print(f"Valor total en stock: {producto3.valor_total()} Gs.")