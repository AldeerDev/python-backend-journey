# 5. invertir_diccionario(d) -> intercambia claves y valores


def invertir_diccionario(d: dict) -> dict:
    return {v: k for k, v in d.items()}
