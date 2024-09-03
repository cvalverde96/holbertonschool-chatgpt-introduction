#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un integer no negativo

    un factorial es el producto de todos los integers
    positivos menos o igual a n
    """

    if n == 0:
        # el factorial de 0 es definido como 1
        return 1
    else:
        return n * factorial(n-1)
        # funcion revursiva que calcula el factorial

f = factorial(int(sys.argv[1]))
# lee el primer argument del command line, ignorando el nombre del programa
print(f)

#imprime dicho calculo
