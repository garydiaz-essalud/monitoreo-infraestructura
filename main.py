# Archivo: main.py 

# 1. Importamos la función específica desde nuestro paquete
from sistema_tickets.reportes import resumen_por_area

# 2. Definimos los datos crudos
tickets = [
    {"id": "T-101", "area": "Farmacia", "tiempo_espera": 45},
    {"id": "T-102", "area": "Admisión", "tiempo_espera": 20},
    {"id": "T-103", "area": "Farmacia", "tiempo_espera": 15},
    {"id": "T-104", "area": "Triaje"} 
]

# 3. Ejecutamos el módulo
print("--- GENERANDO REPORTE MODULARIZADO ---")
resultado = resumen_por_area(tickets)
print(resultado)