"""
Ejercicio 2:
Determina si un año es bisiesto (reglas típicas).
"""

def is_leap_year(year: int) -> bool:
    """
    Devuelve True si el año es bisiesto, False en caso contrario.

    Reglas:
    - Un año es bisiesto si es divisible por 4
    - Excepto si es divisible por 100
    - Pero sí es bisiesto si es divisible por 400
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# --- Pruebas ---
if __name__ == "__main__":
    años = [1900, 2000, 2004, 2023]
    for año in años:
        if is_leap_year(año):
            print(f"El año {año} es bisiesto")
        else:
            print(f"El año {año} NO es bisiesto")