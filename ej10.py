class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.precio} Gs."

class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.subtotal()} Gs."

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total

    def mostrar_detalle(self):
        print("Detalle de la compra")
        for item in self.items:
            print(item)
        print(f"Total general: {self.total()} Gs.")

    def __str__(self):
        return f"Carrito con {len(self.items)} productos"

producto1 = Producto("Galletita", 3000)
producto2 = Producto("Jabón", 4500)
producto3 = Producto("Detergente", 9300)

item1=Item(producto1, 3)
item2=Item(producto2, 2)
item3 = Item(producto3, 1)

carrito =Carrito()

carrito.agregar_item(item1)
carrito.agregar_item(item2)
carrito.agregar_item(item3)

carrito.mostrar_detalle()