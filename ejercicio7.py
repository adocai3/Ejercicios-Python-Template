# coding=utf-8
__Author__ = "José Gaspar Sánchez García"

# Función que genera la serie de Fibonacci hasta n elementos
def fibonacci(n):
    vector = []

    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)
        return vector
    elif n >= 2:
        vector.append(1)
        vector.append(1)
        for i in range(2, n):
            siguiente = vector[i - 1] + vector[i - 2]
            vector.append(siguiente)

    return vector  # Retorno de la función

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introdu
