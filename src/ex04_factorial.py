"""
Ejercicio 4 (un poco más complejo):
Factorial de un número.
"""
def factorial(n: int) -> int:
    """
    Devuelve n! (n factorial).

    Reglas:
    - 0! = 1
    - Si n < 0, lanza ValueError.
    - Debe resolverse usando un bucle (no recursión).
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# --- Pruebas ---
if __name__ == "__main__":
    numeros = [0, 1, 5, -3]
    for num in numeros:
        try:
            print(f"{num}! = {factorial(num)}")
        except ValueError as e:
            print(f"Error con {num}: {e}")
