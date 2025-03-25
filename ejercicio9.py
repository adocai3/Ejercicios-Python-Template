# coding=utf-8
__Author__="José Gaspar Sánchez García"

# Función para sumar
def suma(x, y):
    return x + y

# Función para restar
def resta(x, y):
    return x - y

# Función para multiplicar
def multiplica(x, y):
    return x * y

# Función para dividir
def divide(x, y):
    if y == 0:
        return "Error: No se puede dividir por 0"
    return x / y

# Función que crea el menú de la aplicación
def menuApp():
    print("MENU CALCULADORA")
    opcion = -1

    while opcion != 0:
        print("\n1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion = int(input("Introduzca opción: "))

        if opcion == 1:
            s1 = int(input("Introduzca el primer sumando: "))
            s2 = int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1, s2, suma(s1, s2)))
        elif opcion == 2:
            minuendo = int(input("Introduzca el minuendo: "))
            sustraendo = int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo, sustraendo, resta(minuendo, sustraendo)))
        elif opcion == 3:
            m1 = int(input("Introduzca el primer número para multiplicar: "))
            m2 = int(input("Introduzca el segundo número para multiplicar: "))
            print("La multiplicación de {0} * {1} = {2}.".format(m1, m2, multiplica(m1, m2)))
        elif opcion == 4:
            d1 = int(input("Introduzca el numerador: "))
            d2 = int(input("Introduzca el denominador: "))
            print("La división de {0} / {1} = {2}.".format(d1, d2, divide(d1, d2)))
        elif opcion == 0:
            print("Saliendo de la calculadora.")
        else:
            print("Error: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()

if __name__ == "__main__":
    main()
