DNIs = {
    "A": 43481202,
    "B": 35883893,
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
print("Conjuntos de dígitos únicos:")
for clave, conjunto in conjuntos.items():
    print("\n" + f"DNI {clave} ({DNIs[clave]}) Conjuntos de dígitos únicos:  {conjunto}")
    listaConjuntos = []
    listaConjuntos.append(conjuntos)
    diccionarioDeConjuntos = listaConjuntos[0]

print("\n" + f"Diccionario de conjuntos: {diccionarioDeConjuntos}" + "\n")


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


def conteo_de_frecuencia_digitos_de_cada_dni(DNIs):
    conteo = {}
    for clave, dni in DNIs.items(): # Guardamos el conteo de cada DNI
        conteo[clave] = {} # Inicializamos el conteo para cada DNI
        for digito in str(dni): # Iteramos sobre cada dígito del DNI
            if digito in conteo[clave]: # Si el dígito ya está en el conteo, incrementamos su frecuencia
                conteo[clave][digito] += 1 # Si ya está, lo incrementamos
            else:
                conteo[clave][digito] = 1 # Si no está, lo inicializamos en 1
        print(f"Conteo de frecuencia de DNI{clave}: {conteo[clave]}" ) # Hacemos un print para mostrar el conteo de cada DNI


def suma_total_digitos_de_cada_dni(DNIs):
    suma = {} 
    for clave, dni in DNIs.items(): 
        suma[clave] = sum(int(digito) for digito in str(dni))
        print(f"Suma total de dígitos de DNI{clave}: {suma[clave]}")


def expresion_logica_uno(dic):
    '''Si el conjunto A tiene más elementos que el conjunto B y el conjunto C contiene al menos un número impar, entonces se cumple la condición de combinación amplia.'''
    cont = 0
    for val in dic['C'] :

        if int(val) % 2 == 1:
            cont += 1

    if ((len(dic['A']) >  len(dic['B'])) and cont > 0):
        print('Si el conjunto A tiene más elementos que el conjunto B y el conjunto C contiene al menos un número impar, entonces se cumple la condición de combinación amplia.')
        print(f"A = {len(dic['A'])} y B = {len(dic['B'])}, por lo tanto 'A' es MAYOR que 'B' y C = {dic['C']} contiene al menos {cont} elementos impares")
        print('Por lo que se cumple "la condición de combinación amplia"')


def expresion_logica_dos(dic):
    '''Si algún dígito aparece en todos los conjuntos, se marca como dígito común.'''
    
    # Lógica imperativa sin usar intersection()
    conjuntos_valores = list(dic.values())
    print(conjuntos_valores)
    comunes = set()
    
    # Iteramos sobre cada elemento del primer conjunto
    for elemento in conjuntos_valores[0]:
        esta_en_todos = True
        
        # Verificamos si el elemento está en todos los demás conjuntos
        for conjunto in conjuntos_valores[1:]:
            if elemento not in conjunto:
                esta_en_todos = False
        
        # Si está en todos, lo agregamos a comunes
        if esta_en_todos:
            comunes.add(elemento)
    
    print("Dígitos comunes en todos los conjuntos:", comunes)
    print(comunes)


expresion_logica_dos(diccionarioDeConjuntos)

# print("-----------------------------------------------------")
# print("\n" + "Unión de conjuntos:" + "\n")
# calcular_uniones(diccionarioDeConjuntos)
# print("-----------------------------------------------------")
# print("\n" + "Diferencia entre conjuntos:" + "\n")
# calcular_diferencia(diccionarioDeConjuntos)
# print("-----------------------------------------------------")
# print("\n" + "Intersección entre conjuntos:" + "\n")
# calcular_interseccion(diccionarioDeConjuntos)
# print("-----------------------------------------------------")
# print("\n" + "Diferencia simétrica entre conjuntos:" + "\n")
# calcular_diferencia_simetrica(diccionarioDeConjuntos)
# print("-----------------------------------------------------")
# print("\n" + "Conteo de frecuencia de dígitos de cada DNI:" + "\n")
# conteo_de_frecuencia_digitos_de_cada_dni(DNIs)
# print("-----------------------------------------------------")
# print("\n" + "Suma total de dígitos de cada DNI:" + "\n")
# suma_total_digitos_de_cada_dni(DNIs)
# print("-----------------------------------------------------")
# print("\n" + "1° expresión lógica" + "\n")
# expresion_logica_uno(diccionarioDeConjuntos)
# print("-----------------------------------------------------")
# print("\n" + "2° expresión lógica" + "\n")
# expresion_logica_dos(diccionarioDeConjuntos)
# print("-----------------------------------------------------")
expresion_logica_uno(diccionarioDeConjuntos)
calcular_uniones(diccionarioDeConjuntos)
print("-----------------------------------------------------")
print("\n" + "Diferencia entre conjuntos:" + "\n")
calcular_diferencia(diccionarioDeConjuntos)
print("-----------------------------------------------------")
print("\n" + "Intersección entre conjuntos:" + "\n")
calcular_interseccion(diccionarioDeConjuntos)
print("-----------------------------------------------------")
print("\n" + "Diferencia simétrica entre conjuntos:" + "\n")
calcular_diferencia_simetrica(diccionarioDeConjuntos)
print("-----------------------------------------------------")
print("\n" + "Conteo de frecuencia de dígitos de cada DNI:" + "\n")
conteo_de_frecuencia_digitos_de_cada_dni(DNIs)
print("-----------------------------------------------------")
print("\n" + "Suma total de dígitos de cada DNI:" + "\n")
suma_total_digitos_de_cada_dni(DNIs)
