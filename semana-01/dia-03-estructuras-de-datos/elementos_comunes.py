# 4. elementos_comunes(lista_a, lista_b) ->
# lista de lo que esta en ambas, usando sets


def elementos_comunes(list_a: list, list_b: list) -> list:
    return list(set(list_a) & set(list_b))
