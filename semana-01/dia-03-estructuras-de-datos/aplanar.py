# 8. aplanar(lista_de_listas) -> [[1,2], [3], [4,5]]


def aplanar(lists: list[list]) -> list:
    resultado = []
    for sublista in lists:
        resultado.extend(sublista)
    return resultado

