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
    try:
        # Pedimos al usuario la cantidad de números pares que desea generar
        cantidad = int(input("¿Cuántos números pares deseas generar? "))
        # Pedimos al usuario desde qué número debe comenzar la generación
        inicio = int(input("¿Desde qué número deseas empezar? "))

        # Llamamos a la función para generar los números pares
        pares = generarPares(cantidad, inicio)

        # Mostramos los números pares generados
        print("Números pares generados:", pares)
    
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
