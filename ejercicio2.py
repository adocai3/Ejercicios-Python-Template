def main():
    # Solicita el nombre al usuario
    nombre = input("Introduzca su nombre: ")
    
    # Solicita la edad del usuario
    edad = int(input(f"Introduzca su edad, {nombre}: "))

    # Comprobamos si es mayor de edad
    if edad >= 18:
        print(f"{nombre}, ya puedes conducir.")
    else:
        print(f"{nombre}, todavía no puedes conducir.")

if __name__ == "__main__":
    main()
