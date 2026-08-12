"""Bloque 2 - La clase y el constructor: __init__, self, atributos."""

PRIORIDADES_VALIDAS = ["Baja", "Media", "Alta", "Emergencia"]

class Ticket:
    """Representa un ticket de soporte informático de EsSalud."""

    def __init__(self, codigo, descripcion, area, prioridad):
        self.codigo = codigo
        self.descripcion = descripcion
        self.area = area
        if prioridad not in PRIORIDADES_VALIDAS:
            raise ValueError(f"prioridad invalida: '{prioridad}'")
        self.prioridad = prioridad
        self.estado = "Abierto"  # valor por defecto: todo ticket nuevo nace abierto
    def cerrar(self):
        if self.estado == "Cerrado":
            print(f"{self.codigo}: ya esta cerrado")
        else:
            self.estado = "Abierto"
            print(f"{self.codigo}: Cerrado correctamente")
    def resumen(self):
        return f"[{self.estado}] {self.codigo} - {self.descripcion} ({self.area})"

class TicketUrgente(Ticket):
    """Un ticket que ademas exige un tiempo maximo de atencion (SLA)."""

    def __init__(self, codigo, descripcion, area, sla_minutos):
        super().__init__(codigo, descripcion, area, "Emergencia")
        self.sla_minutos = sla_minutos

    def resumen(self):
        base = super().resumen()
        return f"{base} -- SLA: {self.sla_minutos} min"


if __name__ == "__main__":
    #ticket1 = Ticket("TCK-101", "Impresora no responde", "Emergencia")

    #print(ticket1.codigo)  # TCK-101
    #print(ticket1.descripcion)  # Impresora no responde
    #print(ticket1.estado)  # Abierto

    #ticket2 = Ticket("TCK-102", "Monitor no enciende", "Traumatologia")

    #print(ticket2.codigo)  # TCK-102
    #print(ticket1.codigo)  # TCK-101 -- ticket1 no cambio

   # Dato curioso: type() e isinstance()
    #print(type(ticket1))  
# <class '__main__.Ticket'>
    #print(isinstance(ticket1, Ticket))  # True
    #ticket1.cerrar()
    #print(ticket1.resumen())
    #print(ticket2.resumen())

    #ticket3 = Ticket("TCK-103", "Monitor viejo", "OIS", "Ahora" )
    ticket1 = Ticket("TCK-101", "Impresora no responde", "Emergencia", "Alta")

    try:
        ticket_malo = Ticket("TCK-999", "Prueba", "Farmacia", "Urgentisima")
    except ValueError as error:
        print("No se pudo crear el ticket:", error)

    tickets_hoy = [
    Ticket("TCK-101", "Impresora no responde", "Emergencia", "Alta"),
    Ticket("TCK-102", "Monitor no enciende", "Traumatologia", "Media"),
    Ticket("TCK-103", "Sistema HIS caido", "Emergencia", "Emergencia"),
    ]

    tickets_emergencia = [t for t in tickets_hoy if t.area == "Emergencia"]
    print(len(tickets_emergencia))  # 1

    ticket_urgente = TicketUrgente("TCK-200", "Sistema HIS caido en Emergencia", "Emergencia", 30)
    print(ticket_urgente.resumen())

    print(isinstance(ticket_urgente, Ticket))        # True
    print(isinstance(ticket_urgente, TicketUrgente)) # True