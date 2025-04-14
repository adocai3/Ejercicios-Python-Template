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
        # Inicializamos los dos primeros valores
        vector.append(1)
        vector.append(1)

        # Creamos aquí el bucle WHILE
        contador = 2
        while contador < n:
            siguiente = vector[contador - 1] + vector[contador - 2]
            vector.append(siguiente)
            contador += 1

    return vector  # Retorno
