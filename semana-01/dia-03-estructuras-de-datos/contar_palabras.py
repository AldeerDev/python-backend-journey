# 1. contar_palabras(texto) → diccionario con cuántas veces aparece cada palabra 
# (ignorá mayúsculas y signos básicos)


def contar_palabras(txt: str) -> dict[str, int]:
    """
    Cuenta la cantidad de veces que se repiten las palabras en un texto y 
    devuelve un diccionario.

    Args:
        txt: oración

    Returns:
        Un diccionario con las palabras como claves y como valor un entero
        con la cantidad de veces que aparece la palabra en el texto
    """
    txt = txt.lower()
    txt = "".join(c for c in txt if c.isalnum() or c.isspace())

    contador = {}
    for p in txt.split():
        contador[p] = contador.get(p, 0) + 1

    return contador

if __name__ == '__main__':
    assert contar_palabras("Hola mundo") == {"hola": 1, "mundo": 1}
    assert contar_palabras("") == {}
    assert contar_palabras(" ") == {}
    assert contar_palabras("Hola mundo!, Hola MUNDO") == {"hola": 2, "mundo": 2}
    assert contar_palabras("Hola\nmundo") == {"hola": 1, "mundo": 1}
