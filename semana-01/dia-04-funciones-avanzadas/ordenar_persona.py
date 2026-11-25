def ordenar_personas(personas: list[dict]) -> list[dict]:
    """Devuelve una nueva lista de personas ordenadas por edad, de menor
    a mayor.

    No modifica la lista original.

    Args:
        personas: lista de diccionarios con las claves 'nombre' y 'edad'.

    Returns:
        Nueva lista ordenada por edad.
    """
    return sorted(personas, key=lambda persona: persona["edad"])


if __name__ == '__main__':
    personas = [
        {"nombre": "marta", "edad": 56},
        {"nombre": "andres", "edad": 54},
        {"nombre": "maria", "edad": 31}
    ]

    original = list(personas)
    resultado = ordenar_personas(personas)

    assert [p["nombre"] for p in resultado] == ["maria", "andres", "marta"]
    assert personas == original
    assert ordenar_personas([]) == []
    assert ordenar_personas(personas[:1]) == personas[:1]
