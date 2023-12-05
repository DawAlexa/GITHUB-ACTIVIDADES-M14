"""
TAREA 3 (1.5 puntos).
"""

"""
a)Crea una tupla a partir de una lista. Usa la función constructora de 
tuplas.

"""
lista = [1, 2, 3, 4, 5]

# Llame a la función tupla para crear una tupla a partir de una lista

tupla = tuple(lista)

print(tupla)


"""
b) Crea una lista a partir de una tupla. Usa la función constructora de listas.
"""
# tupla = (1, 2, 3, 4, 5)

# Llame a la función list para crear una lista a partir de una tupla

# lista = list(tupla)

# print(lista)


"""
c)Crea tres listas de dos elementos cada una y luego crea una tupla llamada x que las 
contenga (es decir, algo del estilo: ([1,2], [3,4], [8,2]).
"""
# lista1 = [1, 2]
# lista2 = [3, 4]
# lista3 = [8, 2]

#  Cree una tupla con tres listas

# tupla = (lista1, lista2, lista3)

# print(tupla)


"""
d)Prueba a modificar la posición 0 de la lista que ocupa la posición 0 de la tupla, con: 
¿Has podido realizar la modificación? ¿Cómo es posible, si las tuplas son inmodificables?
"""

# tupla = ((1, 2), (3, 4), (8, 2))

# tupla[0][0] = (10)

# print(tupla)

# Al parecer no logre modifir.