# 2. Mayor de tres números


def mayor_de_tres(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c
