from datetime import datetime

# Contar cuántos años son pares e impares
def contar_pares_impares(anios):
    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

# Verificar si todos son posteriores a 2000
def es_grupo_z(anios):
    # Recorre cada año y si encuentra alguno anterior al 2000, termina la iteración y devuelve Fasle
    for anio in anios:
        if anio <= 2000:
            return False
    return True

# Buscar si un año es bisiesto
def anio_bisiesto(anios):
    bisiestos = []

    for anio in anios:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            bisiestos.append(anio)
    return bisiestos

# Calcular las edades
def calcular_edades(anios):
    # Obtiene el año actual del sistema
    anio_actual = datetime.now().year
    edades = []

    for anio in anios:
        edad = anio_actual - anio
        edades.append(edad)

    return edades

# Calcular el producto cartesiano
def producto_cartesiano(anios, edades):
    combinaciones = []

    for anio in anios:
        for edad in edades:
            combinaciones.append((anio, edad))
    return combinaciones


def main():
    anios_nacimiento = [2001, 1999, 2004, 2000, 1991]

    # Cálculos
    pares, impares = contar_pares_impares(anios_nacimiento)
    grupo_z = es_grupo_z(anios_nacimiento)
    bisiestos = anio_bisiesto(anios_nacimiento)
    edades = calcular_edades(anios_nacimiento)
    cartesiano = producto_cartesiano(anios_nacimiento, edades)

    # Resultados
    print("-----------------------------------------------------")
    print(f"Años ingresados: {anios_nacimiento}")
    print("-----------------------------------------------------")
    print(f"Cantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")
    print("-----------------------------------------------------")

    if grupo_z:
        print("Grupo Z")
    else:
        print("No se cumple la condición que todos los integrantes hayan nacido después del 2000")

    print("-----------------------------------------------------")

    if bisiestos:
        print("Tenemos un año especial.")
        print("Años bisiestos encontrados:", bisiestos)
    else:
        print("No hay años bisiestos.")

    print("-----------------------------------------------------")
    print("Producto cartesiano (año de nacimiento, edad actual):")
    for par in cartesiano:
        print(par)

main()
