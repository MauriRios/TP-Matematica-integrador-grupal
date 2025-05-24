

#Ingreso de los DNIs (reales o ficticios).
#Generación automática de los conjuntos de dígitos únicos.

DNIA = 35883893
DNIB = 40481202
DNIC = 39021321
DNID = 46604396
DNIE = 36441560

DNILista = [DNIA, DNIB, DNIC, DNID, DNIE] 
digitos_unicos = set() # Crear un conjunto para almacenar los dígitos únicos

for i in range(len(DNILista)): # Generación de los conjuntos de dígitos únicos
    # Obtener el DNI actual de la lista
    DNI = DNILista[i]
    # Convertir el DNI a una cadena para poder iterar sobre sus dígitos
    DNI_str = str(DNI)

    # Iterar sobre cada dígito en el DNI
    for digito in DNI_str:
        # Agregar el dígito al conjunto de dígitos únicos
        digitos_unicos.add(digito)
    
    # Imprimir el conjunto de dígitos únicos
    print(f"DNI: {DNI} - Dígitos únicos: {digitos_unicos}")
#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
    print(f"{DNI_str}U{DNI_str} = {set.union(digitos_unicos)}")
    #print(set.intersection(digitos_unicos))
    #print(set.difference(digitos_unicos))
    #print(set.symmetric_difference(digitos_unicos))


DNIs = {
    "A": 35883893,
    "B": 40481202,
    "C": 39021321,
    "D": 46604396,
    "E": 36441560
}

# Generación de los conjuntos de dígitos únicos
conjuntos = {}  # Guardamos los conjuntos de cada DNI

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


