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

    while numeroTirada > 0:
        print(f"Tirada nº {numeroTirada}:")
        
        # Jugada aleatoria para Jugador 1
        j1 = random.choice(["piedra", "papel", "tijera"])
        
        # Jugada aleatoria para Jugador 2
        j2 = random.choice(["piedra", "papel", "tijera"])
        
        print(f"{nombre1} ha sacado {j1}.")
        print(f"{nombre2} ha sacado {j2}.")
        
        ganador = quienGana(j1, j2)
        
        if ganador == 0:
            print("Han empatado.")
        elif ganador == 1:
            print(f"Gana {nombre1}")
            ganadas1 += 1
        elif ganador == 2:
            print(f"Gana {nombre2}")
            ganadas2 += 1
        else:
            print("Error.")
        
        numeroTirada -= 1

    # Resultado final de todas las tiradas
    if ganadas1 == ganadas2:
        print("HAN EMPATADO")
    elif ganadas1 > ganadas2:
        print(f"GANA {nombre1}")
    else:
        print(f"GANA {nombre2}")

if __name__ == "__main__":
    main()

