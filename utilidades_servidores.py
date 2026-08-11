# utilidades_servidores.py

# TUPLA: Definimos los sistemas operativos estandarizados en la red (Inmutable)
SISTEMAS_ESTANDAR = ("Debian", "AlmaLinux", "Windows")

def evaluar_estado_servidor(datos_servidor):
    """
    Evalúa el diccionario de un servidor y retorna su estado de salud.
    """
    # MANEJO DE EXCEPCIONES: Prevenimos que el script se rompa si falta una llave crítica
    try:
        hostname = datos_servidor["hostname"]
        so = datos_servidor["so"]
        
        # DICCIONARIOS: Usamos .get() para evitar errores si 'cpu' no está definido
        cpu_usage = datos_servidor.get("cpu", 0) 
        
        if so not in SISTEMAS_ESTANDAR:
            return f"[ALERTA] El equipo {hostname} corre un SO no estandarizado: {so}"
            
        if cpu_usage > 85:
            return f"[CRÍTICO] {hostname} ({so}) presenta uso de CPU al {cpu_usage}%"
            
        return f"[OK] {hostname} operando dentro de los parámetros."
        
    except KeyError as e:
        return f"[ERROR DEL SISTEMA] Faltan datos vitales en el registro. Falta la llave: {e}"