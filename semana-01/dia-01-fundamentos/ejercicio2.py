# 2. Mayor de tres números


def mayor_de_tres(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    assert mayor_de_tres(5, 5, 3) == 5
    assert mayor_de_tres(3, 5, 5) == 5