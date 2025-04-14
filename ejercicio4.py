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
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"])

        print(f"{nombre1} ha sacado {j1}.")
        print(f"{nombre2} ha sacado {j2}.")

        ganador = quienGana(j1, j2)

        if ganador == 0:
            print("Han empatado.")
        elif ganador == 1:
            ganadas1 += 1
            print(f"Gana {nombre1}. Número de tiradas ganadas --> {ganadas1}")
        elif ganador == 2:
            ganadas2 += 1
            print(f"Gana {nombre2}. Número de tiradas ganadas --> {ganadas2}")
        else:
            print("Error.")

        numeroTirada -= 1
        tirada += 1

    # Resultado final de todas las tiradas
    print("\nRESUMEN FINAL:")
    print(f"{nombre1} --> {ganadas1} victorias.")
    print(f"{nombre2} --> {ganadas2} victorias.")
    if ganadas1 == ganadas2:
        print("HAN EMPATADO.")
    elif ganadas1 > ganadas2:
        print(f"¡{nombre1} GANA!")
    else:
        print(f"¡{nombre2} GANA!")

if __
