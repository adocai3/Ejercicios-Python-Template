# coding=utf-8
# coding=utf-8
__Author__ = "José Gaspar Sánchez García"

import random

# Función que determina si un numero es par.
def esPar(numero):
    return numero % 2 == 0  # Un número es par si el resto de dividir entre 2 es 0

def esImpar(numero):
    return numero % 2 != 0  # Un número es impar si el resto de dividir entre 2 no es 0

def generarPares(valores, inicio):
    pares = []
    numero = inicio
    if esImpar(inicio):  # Si el inicio es impar, empezamos desde el siguiente número par
        numero = inicio + 1
    while len(pares) < valores:  # Generar la cantidad de números que queremos
        pares.append(numero)
        numero += 2  # Pasamos al siguiente número par
    return pares

def generarImpares(valores, inicio):
    impares = []
    numero = inicio
    if esPar(inicio):  # Si el inicio es par, empezamos desde el siguiente número impar
        numero = inicio + 1
    while len(impares) < valores:  # Generar la cantidad de números que queremos
        impares.append(numero)
        numero += 2  # Pasamos al siguiente número impar
    return impares


# Programa principal
def main():
    print("Par e impar")
    
    # Pedimos al usuario un número para verificar si es par o impar
    n = int(input("Introduzca un número: "))
    print("{0} es par --> {1}.".format(n, esPar(n)))
    
    # Pedimos al usuario cuántos números queremos generar
    m = int(input("Introduzca el número de valores: "))
    
    # Pedimos el número inicial para comenzar la generación
    i = int(input("Introduzca el número inicial: "))
    
