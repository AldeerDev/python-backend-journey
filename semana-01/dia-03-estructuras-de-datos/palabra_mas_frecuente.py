# 7. palabra_mas frecuente(texto) -> la que más se repite
from contar_palabras import contar_palabras

def palabra_mas_frecuente(txt: str) -> str:
    conteo = contar_palabras(txt)
    return max(conteo, key=conteo.get) if conteo else ""

