"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre = input("Introduzca su nombre: ")
    edad = int(input(f"Introduzca su edad, {nombre}: "))

    # Comprobamos si es mayor de edad
    if edad >= 18:
        print(f"{nombre}, ya puedes conducir.")
    else:
        print(f"{nombre}, todavía eres menor de edad y no puedes conducir.")

if __name__ == "__main__":
    main()

