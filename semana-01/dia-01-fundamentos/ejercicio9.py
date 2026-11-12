# 9. FizzBuzz del 1 al 100: 
#   múltiplos 
#   de 3 → “Fizz”, 
#   de 5 → “Buzz”, 
#   de ambos → “FizzBuzz”


def fizzbuzz() -> None:
    """
    Imprime los nùmeros del 1 al 100 con las reglas de FizzBuzz.

    - Múltiplo de 3: imprime 'Fizz'.
    - Múltiplo de 5: imprime 'Buzz'.
    - Múltiplo de 3 y 5: imprime 'FizzBuzz'.
    - Cualquier otro número: imprime el número.
    """

    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
