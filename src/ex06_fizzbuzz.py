"""
Ejercicio 6 (un poco más complejo):
FizzBuzz.
"""

def fizzbuzz(n: int) -> list[str]:
    """
    Devuelve una lista con los valores de 1 a n siguiendo las reglas de FizzBuzz.
    """
    # Validación inicial: si n <= 0, devolvemos lista vacía
    if n <= 0:
        return []

    resultado = []
    
    for i in range(1, n + 1):
        # Primero comprobamos la condición más restrictiva (múltiplo de ambos)
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            # Convertimos el número a string para cumplir con el tipo list[str]
            resultado.append(str(i))
            
    return resultado

# Bloque de prueba 
if __name__ == "__main__":
    limite = 15
    print(f"Resultado de FizzBuzz hasta {limite}:")
    print(fizzbuzz(limite))