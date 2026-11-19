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


if __name__ == '__main__':
    assert sumar_todo() == 0
    assert sumar_todo(1) == 1
    assert sumar_todo(1, 2, 3, 4, 5) == 15
    assert sumar_todo(*range(2000)) == 1999000
    assert sumar_todo(1.5, 2.5) == 4.0

    try:
        sumar_todo(1, "")
    except TypeError as e:
        pass
    else:
        raise AssertionError("Debió lanzar TypeError")