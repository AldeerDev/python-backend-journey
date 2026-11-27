from pathlib import Path


def guardar_lineas(ruta: Path, lineas: list[str]) -> None:
    """
    Escribe una linea por elemento, reemplazando el contenido anterior.

    Args:
        ruta: archivo de destino.
        lineas: lineas a escribir, sin salto de linea final.
    """
    with ruta.open('w', encoding='utf-8') as file:
        for linea in lineas:
            file.write(linea + '\n')
    