import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de caracter"

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud <= 0:
                print("La longitud debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    print("Contraseña generada:", contrasena)

if __name__ == "__main__":
    main()