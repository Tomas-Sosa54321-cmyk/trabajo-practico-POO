class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def registrar_nota(self, materia, nota):
        self.notas[materia] = nota

    def promedio(self):
        total = 0
        for nota in self.notas.values():
            total += nota
        return total / len(self.notas)

    def esta_aprobado(self):
        return self.promedio() >= 3

    def __str__(self):
        texto = f"Libreta de calificaciones {self.nombre}\n"
        for materia, nota in self.notas.items():
            texto += f"{materia}: {nota}\n"

        texto += f"Promedio: {self.promedio():.2f}\n"

        if self.esta_aprobado():
            texto += "Condición:Aprobado"
        else:
            texto += "Condición:Reprobado"

        return texto

estudiante = Estudiante("Braulio Jara")

estudiante.registrar_nota("Matemática", 4)
estudiante.registrar_nota("Educación Vial", 5)
estudiante.registrar_nota("Literatura", 3)
estudiante.registrar_nota("Dibujo Técnico", 4)

print(estudiante)