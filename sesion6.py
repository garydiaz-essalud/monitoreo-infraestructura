"""Bloque 1 - Repaso + de diccionario suelto a objeto (por que POO)."""

# Con diccionario (lo que se hizo hasta ahora)
ticket_dict = {"codigo": "TCK-101", "descripcion": "Impresora no responde", "area": "Emergencia", "estado": "Abierto"}


def cerrar_ticket_dict(ticket):
    ticket["estado"] = "Cerrado"


if __name__ == "__main__":
    cerrar_ticket_dict(ticket_dict)
    print(ticket_dict["estado"])  # Cerrado
    print(ticket_dict)