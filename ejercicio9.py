# coding=utf-8
__Author__ = "Adonis Gramaje Victoria"

# Funciones de operaciones matemáticas
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División por cero"
    else:
        return x / y

# Función que crea el menú de la aplicación.
def menuApp():
    print("MENU CALCULADORA")
    opcion = -1

    while opcion != 0:
        print("\n1. Suma")
        print("2. Resta")
        print
