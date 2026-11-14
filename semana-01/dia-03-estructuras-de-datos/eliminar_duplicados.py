# 2. eliminar_duplicados(lista) ->
# lista sin repetidos, manteniendo el orden original.


def eliminar_duplicados(lista: list) -> list:
    sin_duplicados = []
    for i in lista:
        if not i in sin_duplicados:
            sin_duplicados.append(i)

    return sin_duplicados