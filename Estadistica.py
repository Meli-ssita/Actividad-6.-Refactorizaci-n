import math


def intentar_flotante(valor):
    """Convierte de forma segura a float; descarta None y booleanos."""
    if valor is None or isinstance(valor, bool):
        return 0.0, False
    try:
        return float(valor), True
    except (ValueError, TypeError):
        return 0.0, False


def filtrar_datos(lista_cruda):
    """Filtra nulos, tipos incompatibles y valores menores a cero."""
    if not lista_cruda:
        return []

    datos_limpios = []
    for elemento in lista_cruda:
        val_float, es_valido = intentar_flotante(elemento)
        if es_valido and val_float >= 0.0:
            datos_limpios.append(val_float)

    return datos_limpios


def calcular_media(datos):
    """Calcula la media aritmética."""
    if not datos:
        return None
    return sum(datos) / len(datos)


def calcular_varianza(datos, media, es_muestral=True):
    """Calcula la varianza muestral (n-1) o poblacional (n)."""
    n = len(datos)
    if es_muestral:
        if n <= 1:
            return None
        denominador = n - 1
    else:
        if n == 0:
            return None
        denominador = n

    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    return suma_cuadrados / denominador


def generar_resumen(datos, es_muestral=True):
    """Genera el diccionario con las métricas descriptivas."""
    if not datos:
        return None

    media = calcular_media(datos)
    varianza = calcular_varianza(datos, media, es_muestral)
    desviacion = math.sqrt(varianza) if varianza is not None else None

    return {
        "n_observaciones": len(datos),
        "media": media,
        "varianza": varianza,
        "desviacion_estandar": desviacion,
        "tipo_varianza": "muestral (n-1)" if es_muestral else "poblacional (n)",
    }


def ejecutar_pipeline(coleccion_cruda, es_muestral=True):
    """Orquesta el filtrado y el cálculo estadístico."""
    if coleccion_cruda is None:
        return None

    datos_limpios = filtrar_datos(coleccion_cruda)
    return generar_resumen(datos_limpios, es_muestral)


# Ejemplo de uso
if __name__ == "__main__":
    datos_ejemplo = [10, "15.5", None, -3, "error", True, 0, 24.5]
    resultado = ejecutar_pipeline(datos_ejemplo)
    print(resultado)
