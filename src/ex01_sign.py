"""
Ejercicio 1:
Clasifica un número como positivo, negativo o cero.
"""

def sign(n: int) -> str:
    """
    Devuelve:
    - "positivo" si n > 0
    - "negativo" si n < 0
    - "cero" si n == 0
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"


# --- Pruebas ---
if __name__ == "__main__":
    numeros = [10, -5, 0]
    for num in numeros:
        print(f"El número {num} es {sign(num)}")