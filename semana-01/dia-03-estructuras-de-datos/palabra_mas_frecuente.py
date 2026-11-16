# 7. palabra_mas frecuente(texto) -> la que más se repite
from contar_palabras import contar_palabras

def palabra_mas_frecuente(txt: str) -> str:
    """
    Devuelve la palabra con mas frecuencia de un texto.

    Args:
        txt: texto a analizar.

    Returns:
        Palabra que aparece con mas frecuencia. Devuelve la primer palabra
        mas frecuente en caso de empate y una cadena vacia si recibe una
        cadena vacia.
    """
    conteo = contar_palabras(txt)
    return max(conteo, key=conteo.get) if conteo else ""


if __name__ == '__main__':
    texto = "Hola mundo! estamos probando cuantos hola, aparecen en este mundo."
    print(palabra_mas_frecuente(texto))
