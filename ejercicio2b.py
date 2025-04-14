# coding=utf-8
__Author__ = "Adonis Gramaje Victoria"

# Función que determina si la persona es mayor de edad
def esMayorEdad(edad):
    return edad >= 18

# Función principal
def main():
    nombre = input("Introduzca su nombre: ")
    
    try:
        edad = int(input(f"Introduzca su edad, {nombre}: "))
        
        # Usamos la función esMayorEdad para comprobar si puede conducir
        if esMayorEdad(edad):
            print(f"{nombre}, ya puedes conducir.")
        else:
            print(f"{nombre}, todavía no puedes conducir.")
    except ValueError:
        print("Por favor, introduce un número válido para la edad.")

if __name__ == "__main__":
    main()
