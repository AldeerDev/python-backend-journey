# 10. Adivinar un número secreto con while 
# (el programa dice “mayor” o “menor”)
import random


def main():

    n_random = random.randint(1, 100)
    n = int(input("Ingrese un numero del 1 al 100: "))

    while n_random != n:
        if n > n_random:
            print(f"{n} es mayor")
        else:
            print(f"{n} es menor")

        n = int(input("Ingrese un numero del 1 al 100: "))

    print(f"¡Adivinaste! el numero es {n}")


main()
