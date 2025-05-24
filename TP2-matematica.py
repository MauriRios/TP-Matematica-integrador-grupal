DNIs = {
    "A": 35883893,
    "B": 40481202,
    "C": 39021321,
    "D": 46604396,
    "E": 36441560
}

# Generación de los conjuntos de dígitos únicos
conjuntos = {}  # Guardamos los conjuntos de cada DNI
diccionarioDeConjuntos = {} # Guardamos el diccionario de conjuntos  


for clave, dni in DNIs.items():
    # Convertimos el número a string y lo transformamos en conjunto
    conjuntos[clave] = set(str(dni))

# Mostramos los conjuntos generados
print("🔢 Conjuntos de dígitos únicos:")
for clave, conjunto in conjuntos.items():
    print(f"DNI {clave} ({DNIs[clave]}) Conjuntos de dígitos únicos:  {conjunto}")
    listaConjuntos = []
    listaConjuntos.append(conjuntos)
    diccionarioDeConjuntos = listaConjuntos[0]

print(f"Diccionario de conjuntos: {diccionarioDeConjuntos}")


def calcular_uniones(diccionarioDeConjuntos):
    claves = list(diccionarioDeConjuntos.keys())
    resultados = {}

    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):  # solo combina claves distintas y evita repetir
            clave1 = claves[i]
            clave2 = claves[j]
            conjunto1 = diccionarioDeConjuntos[clave1]
            conjunto2 = diccionarioDeConjuntos[clave2]
            union = conjunto1 | conjunto2 # Unión (elementos en conjunto1 o conjunto2 excepto los repetidos)
            clave_union = f"{clave1} ∪ {clave2}"
            resultados[clave_union] = union 
            print(f"{clave_union}: {union}")

    return resultados

def calcular_diferencia(diccionarioDeConjuntos):
    claves = list(diccionarioDeConjuntos.keys())
    resultados = {}

    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):  # solo combina claves distintas y evita repetir
            clave1 = claves[i]
            clave2 = claves[j]
            conjunto1 = diccionarioDeConjuntos[clave1]
            conjunto2 = diccionarioDeConjuntos[clave2]
            union = conjunto1 - conjunto2 # Diferencia (elementos en conjunto1 pero no en conjunto2)
            clave_union = f"{clave1} - {clave2}"
            resultados[clave_union] = union
            print(f"{clave_union}: {union}")

    # Calcular la diferencia en el sentido inverso ya que la diferencia no es conmutativa
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):  # solo combina claves distintas y evita repetir
            clave1 = claves[i]
            clave2 = claves[j]
            conjunto1 = diccionarioDeConjuntos[clave1]
            conjunto2 = diccionarioDeConjuntos[clave2]
            union = conjunto2 - conjunto1 # Diferencia en el sentido inverso ya que no es conmutativa
            clave_union = f"{clave2} - {clave1}" 
            resultados[clave_union] = union
            print(f"{clave_union}: {union}")

    return resultados

def calcular_interseccion(diccionarioDeConjuntos):
    claves = list(diccionarioDeConjuntos.keys())
    resultados = {}

    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):  # solo combina claves distintas y evita repetir
            clave1 = claves[i]
            clave2 = claves[j]
            conjunto1 = diccionarioDeConjuntos[clave1]
            conjunto2 = diccionarioDeConjuntos[clave2]
            union = conjunto1 & conjunto2 # Intersección (elementos comunes en ambos conjuntos)
            clave_union = f"{clave1} ∩ {clave2}"
            resultados[clave_union] = union
            print(f"{clave_union}: {union}")

    return resultados

def calcular_diferencia_simetrica(diccionarioDeConjuntos):
    claves = list(diccionarioDeConjuntos.keys())
    resultados = {}

    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):  # solo combina claves distintas y evita repetir 
            clave1 = claves[i] 
            clave2 = claves[j]
            conjunto1 = diccionarioDeConjuntos[clave1]
            conjunto2 = diccionarioDeConjuntos[clave2] 
            union = conjunto1 ^ conjunto2  # Diferencia simétrica (elementos en conjunto1 o conjunto2, pero no en ambos) 
            clave_union = f"{clave1} ∆ {clave2}" 
            resultados[clave_union] = union 
            print(f"{clave_union}: {union}") 

    return resultados


calcular_uniones(diccionarioDeConjuntos)
calcular_diferencia(diccionarioDeConjuntos)
calcular_interseccion(diccionarioDeConjuntos)
calcular_diferencia_simetrica(diccionarioDeConjuntos)