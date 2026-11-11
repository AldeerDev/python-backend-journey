# 6. Contar vocales de un texto


def contar_vocales(txt: str) -> int:
    vocales = {'a', 'e', 'i', 'o', 'u'}
    cant_vocales = 0
    for letra in txt:

        if letra in vocales:
            cant_vocales += 1

    return cant_vocales
