# coding=utf-8
__Author__ = "José Gaspar Sánchez García"

import random

# Función que determina si un número es par
def esPar(numero):
    return numero % 2 == 0

# Función que determina si un número es impar
def esImpar(numero):
    return not esPar(numero)

# Generar una lista de números pares
def generarPares(valores, inicio):
    pares = []
    numero = inicio
    if esImpar(numero):
        numero += 1  # Asegurar que comienza en par
    for _ in range(valores):
        pares.append
