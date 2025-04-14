def main():
    nombre = input("Introduzca su nombre: ")
    
    try:
        edad = int(input(f"Introduzca su edad, {nombre}: "))
        if edad >= 18:
            print(f"{nombre}, ya puedes conducir.")
        else:
            print(f"{nombre}, todavía no puedes conducir.")
    except ValueError:
        print("Por favor, introduce un número válido para la edad.")

if __name__ == "__main__":
    main()
