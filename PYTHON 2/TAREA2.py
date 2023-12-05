"""
TAREA 2 (1.5 puntos). 
"""

"""
 a)Usa la función map() para crear una lista de números cuyos 
elementos sean el doble de los elementos de otra lista. 
"""

numeros = [1, 2, 3, 4, 5]

# Llame a la función map() para aplicar la función lambda x: x * 2 a cada elemento de la lista numeros

listaDoble = list(map(lambda x: x * 2, numeros))

print(listaDoble)



"""
b)Usa la función map() para crear una lista que convierta a mayúsculas todas las palabras de 
otra lista
Por ejemplo: a partir de la lista palabras=["garza","urraca","gorrión","petirrojo"], 
genere ['GARZA', 'URRACA', 'GORRIÓN', 'PETIRROJO']
"""


palabras = ["garza", "urraca", "gorrión", "petirrojo"]

# Llame a la función map() para aplicar la función lambda x: x.upper() a cada elemento de la lista palabras

listaMayusculas = list(map(lambda x: x.upper(), palabras))

print(listaMayusculas)
