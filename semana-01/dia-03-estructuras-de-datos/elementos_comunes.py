# 4. elementos_comunes(lista_a, lista_b) ->
# lista de lo que esta en ambas, usando sets


def elementos_comunes(list_a: list, list_b: list) -> list:
    """
    Devuelve una lista con los elementos comunes de ambas listas.

    Args:
        list_a: primera lista
        list_b: segunda lista

    Returns
        Nueva lista con elementos comunes de dos listas.
    """

    return list(set(list_a) & set(list_b))
