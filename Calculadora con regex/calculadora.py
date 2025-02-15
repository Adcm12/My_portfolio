import re

def calculadora():
    while True:
        expresion = input("Ingrese la expresión matemática (o 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            break

        # Validar la expresión con Regex
        patron = r'^(\s*[-+]?\d+(\s*[-+*/]\s*[-+]?\d+)+)\s*$'
        if not re.match(patron, expresion):
            print("Expresión inválida. Debe ser una operación matemática básica.")
            continue

        try:
            resultado = eval(expresion)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error al evaluar la expresión:", e)

if __name__ == "__main__":
    calculadora()