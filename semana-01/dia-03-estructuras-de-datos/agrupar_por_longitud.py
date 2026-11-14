# 3. agrupar_por_logitud(lista) ->
# diccionario {3: ["sol", "mar"], 5: ["playa"]}


def agrupar_por_longitud(palabras: list[str]) -> dict[int, str]:
    """
    Agrupa palabras por su longitud.

    Args:
        palabras: lista de palabras

    Returns:
        Devuelve un diccionario con listas de palabras agrupadas por su
        longitud
    """
    grupos = {}

    for palabra in palabras:
        long = len(palabra)
        if not long in grupos.keys():
            grupos[long] = [palabra]
            continue
        grupos[long].append(palabra)

    return grupos
