def sumar_todo(*numeros: int | float) -> float:
    """Devuelve la suma de todos los números recibidos.

    Sin argumentos devuelve 0.

    Args:
        *numeros: numeros a sumar.

    Returns:
        La suma de los argumentos.

    Raises:
        TypeError: si algún argumento no es int ni float
    """
    total = 0
    for n in numeros:
        if not isinstance(n, (int, float)) or isinstance(n, bool):
            raise TypeError(f"Se esperaba 'int' o 'float'. se recibio '{type(n).__name__}'")
        total += n
    return total
