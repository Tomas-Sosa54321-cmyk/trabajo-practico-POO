class Producto:
    def __init__(self, nombre, precio, stock, stock_minimo):
        self.nombre=nombre
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad>0:
            self.stock += cantidad
            print(f"Se ingresaron {cantidad} unidades")
        else:
            print("La cantidad debe ser positiva")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
        elif cantidad > self.stock:
            print("No hay stock suficiente")
        else:
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades")

            if self.stock < self.stock_minimo:
                print("Urgente:Se necesita reponer mercadería")

    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio} Gs.\nStock: {self.stock}\nStock mínimo: {self.stock_minimo}"

producto=Producto("Galletita", 3200, 20, 10)

print(producto)

producto.vender(6)
print(producto)

producto.vender(10)
print(producto)

producto.ingresar_mercaderia(17)
print(producto)

producto.vender(30)
print(producto)