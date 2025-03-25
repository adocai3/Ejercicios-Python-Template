# coding=utf-8
__Author__="José Gaspar Sánchez García"

# Función que genera la secuencia de Fibonacci.
def fibonacci(n):
    vector = []

    # Si n es menor que 1, la secuencia no tiene elementos
    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)  # Si es 1, solo devuelve el primer número
        return vector
    elif n >= 2:
        vector.append(1)  # Primer número de la secuencia
        vector.append(1)  # Segundo número de la secuencia

        # Generar el resto de la secuencia
        for i in range(2, n):
            # El siguiente número es la suma de los dos anteriores
            siguiente = vector[i - 1] + vector[i - 2]
            vector.append(siguiente)
    
    return vector  # Retorna el vector con la secuencia de Fibonacci

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introduzca un número: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero, fibonacci(numero)))

if __name__ == "__main__":
    main()
