# 8. aplanar(lista_de_listas) -> [[1,2], [3], [4,5]]


def aplanar(lists: list[list]) -> list:
    """
    Convierte una lista de listas en una sola lista

    Args:
        lists: lista de listas

    Returns:
        Devuelve una unica lista de una lista de listas
    """
    resultado = []
    for sublista in lists:
        resultado.extend(sublista)
    return resultado


if __name__ == '__main__':
    assert aplanar([[1], [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]
