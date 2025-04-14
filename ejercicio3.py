# coding=utf-8
__Author__ = "Adonis Gramaje Victoria"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utiliza la estructura de control if-elif-else.
- Implemente una función obtenerCalificacion(nota).
"""

# Función que devuelve la calificación según la nota
def obtenerCalificacion(nota):
    if 0 <= nota < 3:
        return "Muy deficiente"
    elif 3 <= nota < 5:
        return "Insuficiente"
    elif 5 <= nota < 6:
        return "Suficiente"
    elif 6 <= nota < 7:
        return "Bien"
    elif 7 <= nota < 9:
        return "Notable"
    elif 9 <= nota <= 10:
        return "Sobresaliente"
    else:
        return None  # En caso de que la nota esté fuera del rango 0-10

# Programa principal
def main():
    try:
        # Solicitar la nota
        n = float(input("Introduzca la nota (0 a 10): "))

        # Validar si la nota está dentro del rango permitido
        if 0 <= n <= 10:
            print("Calificación:", obtenerCalificacion(n))
        else:
            print("Error: La nota debe estar entre 0 y 10.")
    
    except ValueError:
        print("Error: Debe introducir un número válido para la nota.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
