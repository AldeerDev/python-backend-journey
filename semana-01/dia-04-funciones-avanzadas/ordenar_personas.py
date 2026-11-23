def ordenar_personas(personas: list[dict]) -> list[dict]:
    """Devuelve una nueva lista de personas ordenadas por edad, de menor 
    a mayor.

    No modifica la lista original.

    Args:
        personas: lista de diccionarios con las claves 'nombre' y 'edad'.

    Returns:
        Nueva lista ordenada por edad.
    """
    return sorted(personas, key=lambda persona: persona['edad'])


if __name__ == '__main__':
    personas = [
        {'nombre': 'Homero', 'edad': 36},
        {'nombre': 'Lisa', 'edad': 8},
        {'nombre': 'Bart', 'edad': 10},
        {'nombre': 'Maggie', 'edad': 2},
        {'nombre': 'Marge', 'edad': 36}
    ]

    original = list(personas)

    resultado = ordenar_personas(personas)

    assert [p['nombre'] for p in resultado] == ['Maggie', 'Lisa', 'Bart', 'Homero', 'Marge']
    assert personas == original # No modifico la lista original
    assert ordenar_personas([]) == []
    assert ordenar_personas(personas[:1]) == personas[:1]
