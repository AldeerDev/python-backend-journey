# 5. invertir_diccionario(d) -> intercambia claves y valores


def invertir_diccionario(d: dict) -> dict:
    """
    Invierte clave y valor de un diccionario.

    Args:
        d: diccionario cualquiera

    Returns
        Devuelve un nuevo diccionario con clave-valor invertidos
    """
    return {v: k for k, v in d.items()}


if __name__ == '__main__':
    d = {1: "hola", 2: "mundo", 3:("hola", "mundo")}

    assert invertir_diccionario(d) == {"hola": 1, "mundo": 2, ("hola", "mundo"): 3}