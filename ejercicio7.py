# coding=utf-8
__Author__ = "Adonis Gramaje Victoria"

"""
Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores.
"""

import random

# Función que determina quién gana
# 0: Empate
# 1: Gana Jugador 1
# 2: Gana Jugador 2
def quienGana(jugada1, jugada2):
    if jugada1 == jugada2:
        return 0
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "tijera" and jugada2 == "papel") or \
         (jugada1 == "papel" and jugada2 == "piedra"):
        return 1
    else:
        return 2

# Programa principal
def main():
    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    nombre1 = input("Introduzca el nombre del Jugador 1: ")
    nombre2 = input("Introduzca el nombre del Jugador 2: ")
    numeroTirada = int(input("Introduzca el número de tiradas: "))

    ganadas1 = 0
    ganadas2 = 0

    tirada = 1
    while numeroTirada > 0:
        print(f"\nTirada nº {tirada}:")
        j1
