# Archivo: sistema_tickets/reportes.py

def resumen_por_area(tickets):
    try:
        if not tickets:
            raise ValueError("lista vacia")
            
        conteo = {}
        tiempos_totales = {} 
        
        for t in tickets:
            area = t.get("area", "Sin área")
            
            try:
                tiempo = t["tiempo_espera"]
            except KeyError:
                tiempo = 0 
                print(f"[Advertencia] El ticket {t.get('id', 'Desconocido')} no tiene tiempo de espera.")
            
            conteo[area] = conteo.get(area, 0) + 1
            tiempos_totales[area] = tiempos_totales.get(area, 0) + tiempo
            
        promedios = {}
        for area in conteo:
            promedios[area] = tiempos_totales[area] / conteo[area]
            
        return {"conteo": conteo, "promedios": promedios}

    except ValueError:
        return "No hay tickets registrados"