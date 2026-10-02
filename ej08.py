class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion} min.)"

class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion
        return total

    def __str__(self):
        texto = f"Lista: {self.nombre}\n"
        for cancion in self.canciones:
            texto += f"{cancion}\n"
        texto += f"Duración total: {self.duracion_total()} min."
        return texto

cancion1=Cancion("After the Disco", "Broken Bells", 3)
cancion2=Cancion("Ella Qué Me Da", "Cumbia Juan", 2)
cancion3=Cancion("Run to You", "Bryan Adams", 3)

lista = ListaReproduccion("Mis músicas")

lista.agregar_cancion(cancion1)
lista.agregar_cancion(cancion2)
lista.agregar_cancion(cancion3)

print(lista)