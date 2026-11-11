# 4. Tabla de multiplicar de un número


def tabla_de_mult_n(n: int) -> None:
    for factor in range(1, 10):
        print(f"{factor}x{n} = {factor*n}")
