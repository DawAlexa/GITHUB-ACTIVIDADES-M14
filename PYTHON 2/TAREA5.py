""" 
TAREA 5 (1.5 puntos). Declara un diccionario dicc_prefijos para representar una relación 
de provincias españolas y sus prefijos telefónicos. 
dicc_prefijos={} 
Utilizando esa estructura de datos, realiza un fragmento de código en que el usuario pueda
introducir un prefijo telefónico y el programa le devuelva la comunidad autónoma a la que 
pertenece; o añadir un prefijo y una comunidad autónoma nuevos al diccionario. 
(Ver resultado esperado en la página siguiente)
"""


dicc_prefijos = {
    "91": "Madrid",
    "93": "Barcelona",
    "95": "Sevilla",
    "96": "Valencia",
    "97": "Bilbao",
    "98": "Oviedo",
    "99": "Zaragoza",
}

def consulta_prefijo(prefijo):
    if prefijo in dicc_prefijos:
        return dicc_prefijos[prefijo]
    else:
        return None

def add_prefijo(prefijo, comunidad):
    dicc_prefijos[prefijo] = comunidad
    return dicc_prefijos

# Consultar prefijo
prefijo = input("Introduce un prefijo telefónico: ")
comunidad = consulta_prefijo(prefijo)
if comunidad is not None:
    print("El prefijo {} corresponde a la comunidad autónoma de {}".format(prefijo, comunidad))
else:
    print("El prefijo {} no está asociado a ninguna comunidad autónoma".format(prefijo))

# Agrergar34 prefijo
prefijo = input("Introduce un nuevo prefijo telefónico: ")
comunidad = input("Introduce la comunidad autónoma asociada al prefijo: ")
dicc_prefijos = add_prefijo(prefijo, comunidad)
print("El diccionario actualizado es el siguiente:")
print(dicc_prefijos)
