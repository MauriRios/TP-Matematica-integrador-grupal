

#Ingreso de los DNIs (reales o ficticios).
#Generación automática de los conjuntos de dígitos únicos.

DNIA = 35883893
DNIB = 40481202
DNIC = 39021321
DNID = 46604396
DNIE = 36441560

DNILista = [DNIA, DNIB, DNIC, DNID, DNIE] 
# Generación de los conjuntos de dígitos únicos

for i in range(len(DNILista)):
    DNI = DNILista[i]
    # Convertir el DNI a una cadena para poder iterar sobre sus dígitos
    DNI_str = str(DNI)
    # Crear un conjunto para almacenar los dígitos únicos
    digitos_unicos = set()
    
    # Iterar sobre cada dígito en el DNI
    for digito in DNI_str:
        # Agregar el dígito al conjunto de dígitos únicos
        digitos_unicos.add(digito)
    
    # Imprimir el conjunto de dígitos únicos
    print(f"DNI: {DNI} - Dígitos únicos: {digitos_unicos}")
#Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
    print(set.union(digitos_unicos))
    #print(set.intersection(digitos_unicos))
    #print(set.difference(digitos_unicos))
    #print(set.symmetric_difference(digitos_unicos))





   