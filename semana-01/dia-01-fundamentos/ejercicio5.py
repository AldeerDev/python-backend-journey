# 5. Factorial de un número


def factorial(n: int) -> int:
    """
    Calcula el factorial de un numero n.

    Args:
        n: numero entero

    Returns:
        Devuelve el factorial de n.
    """
    resultado = 1
    
    for factor in range(1, n+1):
        resultado *= factor
    return resultado


if __name__ == '__main__':
    assert factorial(0) == 1
