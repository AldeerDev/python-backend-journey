from collections.abc import Callable

def crear_multiplicador(n: int) -> Callable[[int], int]:
    return lambda m: n*m
