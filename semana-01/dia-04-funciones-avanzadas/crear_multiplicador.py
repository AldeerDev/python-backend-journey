from collections.abc import Callable

def crear_multiplicador(n: int) -> Callable[[int], int]:
    """Crea una función que multiplica un número por un factor fijo.
    
    Args:
        n: Factor por el cual se multiplicará el número recibido

    Returns:
        Una función que recibe un entero y devuelve su producto
        por el factor n.

    Example:
        >>> duplicar = crear_multiplicador(2)
        >>> duplicar(5)
        10

        >>> triplicar = crear_multiplicador(3)
        >>> triplicar(5)
        15
    """
    return lambda m: n*m
