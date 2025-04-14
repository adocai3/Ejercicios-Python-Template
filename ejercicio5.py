# coding=utf-8
__Author__ = "Adonis Gramaje Victoria"

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
        numero += 1  # Asegurar que empieza en un número par
    for _ in range(valores):
        pares.append(numero)
        numero += 2  # Aumentamos de dos en dos para generar pares
    return pares

# Programa principal para probar la función
def main():
    cantidad = int(input("¿Cuántos números pares deseas generar? "))
    inicio = int(input("¿Desde qué número deseas empezar? "))

    pares = generarPares(cantidad, inicio)
    print("Números pares generados:", pares)

if __name__ == "__main__":
    main()
