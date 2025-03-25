# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.
def esMayorEdad(edad):
    """Función que devuelve True si la edad es mayor o igual a 18, False en caso contrario."""
    return edad >= 18

# Programa principal
def main():
    nombre = input("Introduzca su nombre: ")
    edad = int(input(f"Introduzca su edad, {nombre}: "))

    # Utilizamos la función definida
    if esMayorEdad(edad):
        print(f"{nombre}, ya puedes conducir.")
    else:
        print(f"{nombre}, todavía eres menor de edad y no puedes conducir.")

if __name__ == "__main__":
    main()
