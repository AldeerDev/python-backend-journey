# 1. contar_palabras(texto) → diccionario con cuántas veces aparece cada palabra 
# (ignorá mayúsculas y signos básicos)


def contar_palabras(txt: str) -> dict:
    """
    Cuenta la cantidad de veces que se repiten las palabras en un texto y 
    devuelve un diccionario.

    Args:
        txt: oración

    Returns:
        Un diccionario con las palabras como claves y como valor un entero
        con la cantidad de veces que aparece la palabra en el texto
    """