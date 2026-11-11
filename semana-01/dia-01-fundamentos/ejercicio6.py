# 6. Contar vocales de un texto


def contar_vocales(txt: str) -> int:
    """
    Devuelve la cantidad de vocales que tiene una cadena.
    (no cuenta vocales con tilde {'á', 'é', 'í', 'ó', 'ú'})

    Args:
        txt: cadena de texto

    Returns:
        Retorna el numero de vocales.
    """
    
    vocales = {'a', 'e', 'i', 'o', 'u'}
    cant_vocales = 0
    for letra in txt:

        if letra in vocales:
            cant_vocales += 1

    return cant_vocales
