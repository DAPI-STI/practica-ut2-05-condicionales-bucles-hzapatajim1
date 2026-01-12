"""
Ejercicio 5:
Tabla de multiplicar.
"""

def multiplication_table(n: int) -> list[int]:
    """
    Devuelve una lista con 10 elementos:
    [n*1, n*2, ..., n*10]
    """
    # Usamos una lista por comprensión para generar los 10 valores
    return [n * i for i in range(1, 11)]

# Bloque de prueba para ejecutar
if __name__ == "__main__":
    numero = int(input("Introduce un número para ver su tabla: "))
    resultado = multiplication_table(numero)
    print(f"Tabla del {numero}: {resultado}")
