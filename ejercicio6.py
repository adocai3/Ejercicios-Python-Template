# coding=utf-8
__Author__="José Gaspar Sánchez García"

# Función que determina si un número es primo.
def esPrimo(numero):
    if numero <= 1:  # Los números menores o iguales a 1 no son primos
        return False

    # Bucle para verificar si el número tiene divisores
    for i in range(2, int(numero ** 0.5) + 1):  # Solo verificamos hasta la raíz cuadrada de 'numero'
        if numero % i == 0:  # Si es divisible por 'i', no es primo
            return False
    
    return True  # Si no tiene divisores, es primo

# Programa principal
def main():
    print("ES PRIMO")
    n = int(input("Introduzca un número: "))
    print("{0} es primo --> {1}.".format(n, esPrimo(n)))

if __name__ == "__main__":
    main()
