from pathlib import Path
import tempfile


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


def leer_lineas(ruta: Path) -> list[str]:
    """Devuelve las líneas por elemento, reemplazando el contenido anterior.

    Args:
        ruta: archivo a leer.

    Returns:
        Lista de líneas. Un archivo vacío devuelve [].
    """
    with ruta.open('r', encoding='utf-8') as file:
        return [linea.rstrip('\n') for linea in file]


def agregar_linea(ruta: Path, linea: str) -> None:
    """Escribe una nueva linea al final del archivo, sin borrar lo anterior.
    
    Args:
        ruta: archivo de destino.
        linea: texto a agregar, sin salto de línea final.
    """
    with ruta.open('a', encoding='utf-8') as file:
        file.write(linea + '\n')
    