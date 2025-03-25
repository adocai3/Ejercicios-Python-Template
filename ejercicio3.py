# coding=utf-8
__author__ = "José Gaspar Sánchez García"
"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente.
- Utilice la estructura de control if-elif-else.
- Implemente una función obtenerCalificacion(nota)."""

# Implementación de la función obtenerCalificacion
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
        return "Nota incorrecta"

# Programa principal
def main():
    try:
        n = float(input("Introduzca la nota: "))  # Se usa float para aceptar decimales
        print("Calificación:", obtenerCalificacion(n))
    except ValueError:
        print("Error: Debe introducir un número válido.")

if __name__ == "__main__":
    main()

