# 9. FizzBuzz del 1 al 100: 
#   múltiplos 
#   de 3 → “Fizz”, 
#   de 5 → “Buzz”, 
#   de ambos → “FizzBuzz”


def fizzbuzz() -> None:
    """
    Imprime por pantalla:
        'Fizz' -> cuando el numero es multiplo de 3
        'Buzz' ->  cuando el numero es multiplo de 5
        'FizzBuzz' -> cuando es multiplo de 3 y 5
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
