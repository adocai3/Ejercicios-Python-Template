# coding=utf-8
import random

# Función que determina quién gana Piedra, papel o tijera
# 0: Empate.
# 1: Gana Jugador 1.
# 2: Gana Jugador 2.

def quienGana(jugada1, jugada2):
    if jugada1 == jugada2:
        return 0  # Empate
    elif jugada1 == "piedra" and jugada2 == "tijera":
        return 1  # Gana Jugador 1
    elif jugada1 == "tijera" and jugada2 == "papel":
        return 1  # Gana Jugador 1
    elif jugada1 == "papel" and jugada2 == "piedra":
        return 1  # Gana Jugador 1
    else:
        return 2  # Gana Jugador 2

# Programa principal
def main():
    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    nombre1 = input("Introduzca el nombre del Jugador 1: ")
    nombre2 = input("Introduzca el nombre del Jugador 2: ")
    numeroTirada = int(input("Introduzca el número de tiradas: "))

    ganadas1 = 0
    ganadas2 = 0
    empates = 0

    while numeroTirada > 0:
        print(f"Tirada nº {numeroTirada}:")
        
        # Jugadas aleatorias para ambos jugadores
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"])
        
        # Mostrar las jugadas de ambos jugadores
        print(f"{nombre1} ha sacado {j1}.")
        print(f"{nombre2} ha sac
