# 6. cuadrados_pares(n) -> lista de cuadrados de los números pares del 1 a n,
# con comprensión de listas


def cuadrados_pares(n: int) -> list[int]:
    """
    Devuelve una lista con cuadrados pares del 1 a n

    Args:
        n: iterador

    Returns:
        Lista de cuadrados pares.
    """
    return [x**2 for x in range(1, n+1) if x % 2 == 0]