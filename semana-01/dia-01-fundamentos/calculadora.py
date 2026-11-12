def sumar(a: int, b: int) -> int:
    """
    Suma los numeros enteros a y b.

    Args:
        a: número entero.
        b: número entero.

    Returns:
        Retorna el resultado de la suma de a y b.
    """
    return a + b


def restar(a: int, b: int) -> int:
    """
    Realiza la resta entre a y b, devolviendo el resultado.

    Args:
        a: minuendo.
        b: sustraendo.

    Returns:
        Retorna el resultado de la sustraccion a y b.
    """
    return a - b


def multiplicar(a: int, b: int) -> int:
    """
    Realiza la operacion de multiplicacion entre a y b.

    Args:
        a: factor.
        b: factor.

    Returns:
        Retorna el resultado de la operacion de multiplicacion entre a y b.
    """
    return a * b


def dividir_entero(a: int, b: int) -> int:
    """
    Realiza la operacion de divison entera entre a y b.

    Args:
        a: dividendo.
        b: divisor, no puede ser cero.

    Returns:
        El cocinete de a entre b.

    Raises:
        ZeroDivisionError: si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("'b' no puede ser igual a 0")

    return a // b
    