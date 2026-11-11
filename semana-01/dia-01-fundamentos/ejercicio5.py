# 5. Factorial de un número


def factorial(n: int) -> int:
    resultado = 1
    for factor in range(1, n+1):
        resultado *= factor
    return resultado
