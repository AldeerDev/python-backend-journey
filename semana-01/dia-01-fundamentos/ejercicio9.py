# 9. FizzBuzz del 1 al 100: 
#   múltiplos 
#   de 3 → “Fizz”, 
#   de 5 → “Buzz”, 
#   de ambos → “FizzBuzz”


def fizzbuzz() -> None:
    for n in range(101):
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} - FizzBuzz")
        elif n % 3 == 0:
            print(f"{n} - Fizz")
        elif n % 5 == 0:
            print(f"{n} - Buzz")
