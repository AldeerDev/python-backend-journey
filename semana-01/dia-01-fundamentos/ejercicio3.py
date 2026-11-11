# 3. Suma de los números del 1 al N


def sumar_uno_a_n(n: int) -> int:
    sumatoria = 0
    for i in range(1, n + 1):
        sumatoria += i
    return sumatoria
