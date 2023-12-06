""" 
TAREA 6 (2 puntos) Crea un programa que a) pida al usuario una cadena de texto de 
cualquier número de palabras; b)cuente las ocurrencias de cada palabras que hay en esa 
cadena (utiliza el método split para separar palabras); c)que vaya almacenando la 
información en un diccionario; y d)printe el diccionario por pantalla. 
Resultado esperado: 
"""

def contar_ocurrencias(cadena):
    diccionario = {}
    for palabra in cadena.split():
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


cadena = input("Introduce una cadena de texto: ")
diccionario = contar_ocurrencias(cadena)
print("El diccionario de ocurrencias es el siguiente:")
print(diccionario)
