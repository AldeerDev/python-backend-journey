# 2. eliminar_duplicados(lista) ->
# lista sin repetidos, manteniendo el orden original.


def eliminar_duplicados(lista: list) -> list:
    """
    Elimina duplicados de una lista.

    Args:
        lista: lista con elementos duplicados.

    Returns:
        Devuelve una nueva lista sin elementos duplicados.
    """
    return list(dict.fromkeys(lista))


if __name__ == '__main__':
    assert eliminar_duplicados(["manzana", "banana", "manzana", "limon"]) == ["manzana", "banana", "limon"]
    assert eliminar_duplicados([1,2,3,3,4,6,10]) == [1,2,3,4,6,10]
    assert eliminar_duplicados(["manzana", 1, 2, 2, None, None]) == ["manzana", 1, 2, None]
