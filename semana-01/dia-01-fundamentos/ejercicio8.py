# 8. Verificar si una palabra es palindromo


def palindromo(palabra: str) -> bool:
    """
    Devuelve verdadero o falso si una palabra es palindromo.

    Args:
        palabra:

    Returns:
        Retorna True si la palabra es palindromo, o False
        sino.
    """
    palabra = palabra.lower().strip()
    index_i = 0
    index_f = len(palabra) - 1

    for pos in range(len(palabra) // 2):
        if palabra[index_i + pos] != palabra[index_f - pos]:
            return False

    return True
