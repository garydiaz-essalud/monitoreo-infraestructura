"""
BLOQUE 7 - ACTIVIDAD PRÁCTICA
Modelar equipos de cómputo con clases
Archivo: bloque7_ejercicio_equipos.py
"""


# 1. Clase Equipo
class Equipo:
    """Representa un equipo de cómputo de la institución."""

    def __init__(self, codigo, tipo, area):
        self.codigo = codigo
        self.tipo = tipo
        self.area = area
        self.estado = "Operativo"  # Valor por defecto

    # 2. Dos métodos
    def marcar_en_mantenimiento(self):
        """Cambia el estado a En Mantenimiento e imprime un aviso."""
        self.estado = "En Mantenimiento"
        print(f"AVISO: El equipo {self.codigo} ha sido marcado como En Mantenimiento.")

    def marcar_operativo(self):
        """Cambia el estado a Operativo e imprime un aviso."""
        self.estado = "Operativo"
        print(f"AVISO: El equipo {self.codigo} ha vuelto a estar Operativo.")

    # 3. resumen(self)
    def resumen(self):
        """Devuelve el estado del equipo con el formato '[estado] codigo (tipo) - area'."""
        return f"[{self.estado}] {self.codigo} ({self.tipo}) - {self.area}"

class Impresora(Equipo):
    """Subclase de Equipo que agrega gestión del nivel de tinta."""

    def __init__(self, codigo, area, nivel_tinta=100):
        # Llama al constructor padre asignando el tipo fijo "Impresora"
        super().__init__(codigo, "Impresora", area)
        self.nivel_tinta = nivel_tinta

    def marcar_en_mantenimiento(self):
        # Mantiene el mensaje y cambio de estado original usando super()
        super().marcar_en_mantenimiento()
        # Agrega la impresión del nivel de tinta restante
        print(f"Nivel de tinta restante: {self.nivel_tinta}%")

# 4. Lista + filtro
if __name__ == "__main__":
    # Crear 3+ objetos Equipo
    equipo1 = Equipo("EQ-101", "Impresora", "Emergencia")
    equipo2 = Equipo("EQ-102", "Monitor", "Traumatología")
    equipo3 = Equipo("EQ-103", "PC de Escritorio", "Farmacia")
    equipo4 = Equipo("EQ-104", "Lector Cédula", "Emergencia")

    equipos = [equipo1, equipo2, equipo3, equipo4]

    # Marcar uno en mantenimiento
    equipo1.marcar_en_mantenimiento()

    print("\n--- Todos los equipos ---")
    for eq in equipos:
        print(eq.resumen())

    # Filtrar con comprensión de lista
    equipos_en_mantenimiento = [e for e in equipos if e.estado == "En Mantenimiento"]

    print("\n--- Equipos en Mantenimiento ---")
    for eq in equipos_en_mantenimiento:
        print(eq.resumen())

    equipo1.marcar_operativo()

    print("\n--- Todos los equipos ---")
    for eq in equipos:
        print(eq.resumen())

    # Filtrar con comprensión de lista
    equipos_en_mantenimiento = [e for e in equipos if e.estado == "En Mantenimiento"]

    print("\n--- Equipos en Mantenimiento ---")
    for eq in equipos_en_mantenimiento:
        print(eq.resumen())

    inventario = [
    Equipo("PC-014", "Computadora", "Admision"),
    Equipo("IMP-003", "Impresora", "Emergencia"),
    Equipo("PC-027", "Computadora", "Farmacia"),
    ]

    inventario[1].marcar_en_mantenimiento()

    en_mantenimiento = [e for e in inventario if e.estado == "En Mantenimiento"]
    print(len(en_mantenimiento))  # 1

    for e in inventario:
        print(e.resumen())    

    impresora1 = Impresora("IMP-001", "Emergencia", nivel_tinta=45)
    
    # Probar el método anulado
    impresora1.marcar_en_mantenimiento()
    
    # Probar resumen heredado
    print(impresora1.resumen())