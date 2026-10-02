class Turno:
    def __init__(self, paciente, hora, estado):
        self.paciente=paciente
        self.hora=hora
        self.estado=estado

    def atender(self):
        self.estado = "Atendido"

    def __str__(self):
        return f"Paciente: {self.paciente} -  Hora: {self.hora} -  Estado: {self.estado}"


class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print("Turnos Pendientes")
        for turno in self.turnos:
            if turno.estado == "Pendiente":
                print(turno)

    def __str__(self):
        texto = "Agenda de este día\n"
        for turno in self.turnos:
            texto += f"{turno}\n"
        return texto

turno1 =Turno("Braulio Jara", "09:00", "Pendiente")
turno2= Turno("Brenda Armoa", "10:00", "Pendiente")
turno3= Turno("Carlos Garcia", "11:00", "Pendiente")
turno4 =Turno("Jesús Sosa", "12:00", "Pendiente")

agenda = Agenda()

agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)
agenda.agregar_turno(turno4)

turno1.atender()
turno3.atender()

print(agenda)
print()
agenda.listar_pendientes()