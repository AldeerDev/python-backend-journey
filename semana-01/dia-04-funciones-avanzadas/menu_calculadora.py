def sumar(a: int | float, b: int | float) -> int | float:
    """
    Suma los numeros a y b.
    
    Args:
        a: primer sumando
        b: segundo sumando
    
    Returns:
        Devuelve el resultado de la suma
    """
    return a + b


def restar(a: int | float, b: int | float) -> int | float:
    """
    Realiza la operacion resta entre a y b

    Args:
        a: minuendo
        b: sustraendo

    Returns:
        Devuelve el resultado de a - b
    """
    return a - b

def multiplicar(a: int | float, b: int | float) -> int | float:
    """
    Realiza la operacion de multiplicacion entre a y b.

    Args:
        a: primer factor
        b: segundo factor

    Returns:
        Devuelve el resultado de multiplicar a * b
    """
    return a * b

def dividir(a: int | float, b: int | float) -> float:
    """
    Realiza la operacion de division real a / b

    Args:
        a: dividendo
        b: divisor

    Returns:
        Devuelve el resultado de a / b
    """
    return a / b

def mostrar_menu() -> None:
    """
    Muestra un menu con las operaciones basicas de matematica
    """
    print("1. Sumar.")
    print("2. Restar.")
    print("3. Multiplicar.")
    print("4. Dividir.")
    print("5. Salir.")

def separador() -> None:
    """Imprime 20 giones de separacion."""
    print("-"*20)

def main() -> None:
    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir,
        "5": "salir"
    }

    while True:
        mostrar_menu()
        opcion = input("Elegi una opcion: ")

        if not opcion or not operaciones.get(opcion, None):
            print("continua")
            continue

        if operaciones.get(opcion) == "salir":
            break

        separador()
        try:
            operacion = operaciones.get(opcion)
            a = float(input("Ingresa el valor de a: "))
            b = float(input("Ingresa el valor de b: "))
            resultado = operacion(a, b)
            print("Resultado:", resultado)
            separador()
        except ZeroDivisionError:
            print("No se puede dividir por 0.")
            separador()
            continue
        except ValueError:
            print("Debes ingresar un numero.")
            separador()
            continue


if __name__ == '__main__':
    main()
