"""
Ejercicio 3:
Suma de los primeros n números.
"""

def sum_first_n(n: int) -> int:
    """
    Devuelve la suma 1 + 2 + ... + n.

    - Si n <= 0, devuelve 0.
    - Debe resolverse usando un bucle (for o while).
    """
    if n <= 0:
        return 0

    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


# --- Pruebas ---
if __name__ == "__main__":
    numeros = [5, 10, 0, -3]
    for num in numeros:
        print(f"La suma de los primeros {num} números es {sum_first_n(num)}")
