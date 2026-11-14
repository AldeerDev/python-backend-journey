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

    sin_duplicados = []
    for i in lista:
        if not i in sin_duplicados:
            sin_duplicados.append(i)

