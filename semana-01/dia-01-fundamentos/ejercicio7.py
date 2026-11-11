# 7. Invertir un texto


def invertir_texto(txt: str) -> str:
    longitud = len(txt)
    txt_invertido = ""
    for i in range(longitud):
        txt_invertido += txt[-1]
        txt = txt[:-1]
    return txt_invertido
