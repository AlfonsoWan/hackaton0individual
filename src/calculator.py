# src/calculator.py

def add(a, b):
    """Realiza la suma de dos números."""
    return a + b

def subtract(a, b):
    """Realiza la resta de dos números."""
    return a - b

def multiply(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b

def divide(a, b):
    """Realiza la división de dos números. Lanza un error si se intenta dividir entre cero."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")  # Manejo de errores [[2]]
    return a / b

if __name__ == "__main__":
    print("Bienvenido a la Calculadora en Línea de Comandos!")
    while True:
        try:
            # Solicitar entrada del usuario
            operation = input("Ingrese la operación (ejemplo: '2 + 3') o escriba 'salir' para terminar: ").strip()
            
            if operation.lower() == "salir":
                print("¡Gracias por usar la calculadora!")
                break
            
            # Procesar la entrada
            parts = operation.split()
            if len(parts) != 3:
                print("Formato incorrecto. Use 'a operador b'.")
                continue
            
            a, operator, b = parts
            a, b = float(a), float(b)
            
            # Realizar la operación
            if operator == "+":
                result = add(a, b)
            elif operator == "-":
                result = subtract(a, b)
            elif operator == "*":
                result = multiply(a, b)
            elif operator == "/":
                result = divide(a, b)
            else:
                print("Operador no soportado. Use '+', '-', '*', '/'.")
                continue
            
            # Mostrar el resultado
            print(f"Resultado: {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
