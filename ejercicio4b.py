# coding=utf-8
__Author__ = "Adonis Gramaje Victoria"

"""
Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores.
"""

import random

# Función que determina quién gana Piedra, papel o tijera
# 0: Empate.
# 1: Gana Jugador 1.
# 2: Gana Jugador 2.
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
    empates = 0
    tirada_actual = 1

    while numeroTirada > 0:
        print("\nTirada nº {}:".format(tirada_actual))
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"])

        # Mostrar jugadas usando format
        print("{} ha sacado {}.".format(nombre1, j1))
        print("{} ha sacado {}.".format(nombre2, j2))

        ganador = quienGana(j1, j2)

        if ganador == 0:
            empates += 1
            print("Han empatado.")
        elif ganador == 1:
            ganadas1 += 1
            print("Gana {} la tirada {}. Número de tiradas ganadas --> {}".format(nombre1, tirada_actual, ganadas1))
        elif ganador == 2:
            ganadas2 += 1
            print("Gana {} la tirada {}. Número de tiradas ganadas --> {}".format(nombre2, tirada_actual, ganadas2))
        else:
            print("Error.")

        numeroTirada -= 1
        tirada_actual += 1

    # Mostrar resumen final
    print("\nRESUMEN:\n\t{} --> {} victorias.\n\t{} --> {} victorias.\n\tEmpates: {}".format(
        nombre1, ganadas1, nombre2, ganadas2, empates))

    if ganadas1 == ganadas2:
        print("HAN EMPATADO")
    elif ganadas1 > ganadas2:
        print("GANA {} ({})".format(nombre1, ganadas1))
    else:
        print("GANA {} ({})".format(nombre2, ganadas2))

if __name__ == "__main__":
    main()
