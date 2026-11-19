def sumar_todo(*numeros: int | float) -> float:
        if not isinstance(n, (int, float)) or isinstance(n, bool):
            raise TypeError(f"Se esperaba 'int' o 'float'. se recibio '{type(n).__name__}'")
        total += n
    return total

