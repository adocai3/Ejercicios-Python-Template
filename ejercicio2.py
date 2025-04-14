def main():
    nombre = input("Introduzca su nombre: ")
    edad = int(input(f"Introduzca su edad, {nombre}: "))

    # Comprobamos si es mayor de edad - Estructura condicional if - else
    # Si edad mayor o igual a dieciocho --> Usted es mayor de edad
    # Sino --> Todavía eres menor de edad
    if edad >= 18:
        print(f"{nombre}, ya puedes conducir.")
    else:
        print(f"{nombre}, todavía no puedes conducir.")

if __name__ == "__main__":
    main()
