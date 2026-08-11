# ============================================================
# BLOQUE 8 - Ejercicio guiado: "Resumen de tickets por area"
# Curso Python EsSalud - Sesion 4
# ============================================================
# TODO: completa el codigo para que:
#   1. Defina una lista de diccionarios, donde cada diccionario representa
#      un ticket con "id", "area" y "tiempo_espera".
#   2. Defina una funcion resumen_por_area(tickets) que devuelva un diccionario
#      contando cuantos tickets hay por cada area (patron del bloque 6).
#   3. Use try/except para manejar el caso de que la lista de tickets este vacia
#      (usar el patron del bloque 7).
#   4. Llame a la funcion e imprima el resultado.

def resumen_por_area(tickets):
    try:
        # 1. Primer manejo de error: Lista vacía (Ya lo tenías)
        if not tickets:
            raise ValueError("lista vacia")
            
        conteo = {}
        tiempos_totales = {} # Nuevo diccionario para sumar los tiempos
        
        for t in tickets:
            area = t.get("area", "Sin área")
            
            # 2. Segundo manejo de error: Capturamos si falta "tiempo_espera"
            try:
                tiempo = t["tiempo_espera"]
            except KeyError:
                tiempo = 0 # Si no hay tiempo, asumimos 0 para no romper el script
                print(f"[Advertencia] El ticket {t.get('id', 'Desconocido')} no tiene tiempo de espera registrado.")
            
            # Contamos los tickets por área
            conteo[area] = conteo.get(area, 0) + 1
            # Sumamos los tiempos por área
            tiempos_totales[area] = tiempos_totales.get(area, 0) + tiempo
            
        # Calculamos el promedio
        promedios = {}
        for area in conteo:
            promedios[area] = tiempos_totales[area] / conteo[area]
            
        return {"conteo": conteo, "promedios": promedios}

    except ValueError:
        return "No hay tickets registrados"

tickets = [
    {"id": "T-101", "area": "Farmacia", "tiempo_espera": 45},
    {"id": "T-102", "area": "Admisión", "tiempo_espera": 20},
    {"id": "T-103", "area": "Farmacia", "tiempo_espera": 10},
    {"id": "T-104", "area": "Admisión", "tiempo_espera": 20},
    {"id": "T-105", "area": "Farmacia", "tiempo_espera": 30},
    {"id": "T-106", "area": "Admisión", "tiempo_espera": 40},
    {"id": "T-107", "area": "Admisión", "tiempo_espera": 50},
    {"id": "T-108", "area": "Admisión", "tiempo_espera": 20},
    {"id": "T-109", "area": "Farmacia", "tiempo_espera": 20},
    {"id": "T-110", "area": "Farmacia", "tiempo_espera": 10},
    {"id": "T-111", "area": "Farmacia", "tiempo_espera": 10},
]

print(resumen_por_area(tickets))   # {'Farmacia': 2, 'Admisión': 1}
print(resumen_por_area([]))         # No hay tickets registrados

# ------------------------------------------------------------
# RETO EXTRA (para quien termine antes):
# Agrega a la funcion un segundo try/except que capture KeyError
# si algun ticket no tiene la clave "tiempo_espera", y calcula
# ademas el tiempo de espera promedio por area usando esa clave.
# ------------------------------------------------------------