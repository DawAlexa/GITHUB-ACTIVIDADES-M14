"""
TAREA 4 (1.5 puntos). Utiliza una lista para representar una cola de pedidos en un almacén: 
cola_pedidos = [pedido345671, pedido628316, pedido235252, ...] 
Programa tres funciones: 
(NOTA: usa los métodos propios de las listas: pop, append...)
"""


"""
a)Una función procesarPedido que saque el primer pedido de la cola y lo muestre por 
pantalla. Ej: “Procesando pedido345671....”
"""

# almacen = [345671, 628316, 235252] 

# def procesarPedido(cola_pedidos):
#     # Sacamos el primer pedido de la cola
#     pedido = cola_pedidos.pop(0)
 
#     # Muestro el pedido por pantalla
#     print("Procesando pedido", almacen, "...")

#     return pedido

# procesarPedido(almacen)

"""
b)Una función encolarPedido que añada un pedido al final de la lista. 
"""
# almacen = [345671, 628316, 235252]
# nuevo_pedido= 222

# def encolarPedido(cola_pedidos, pedido):
#     # Añado el pedido al final de la cola
#     cola_pedidos.append(pedido)
    
#     print("Este es su pedido final",cola_pedidos)
#     return cola_pedidos

# encolarPedido(almacen,nuevo_pedido)

"""
c)Una función vaciarCola que elimine todos los pedidos de la lista. 
"""
# almacen = [345671, 628316, 235252]

# def vaciarCola(cola_pedidos):
#     # Elimino todos los pedidos de la cola
#     while len(cola_pedidos) > 0:
#         cola_pedidos.pop(0)

#     return cola_pedidos

# vaciarCola(almacen)
# print (almacen)

"""
d)Con listas podemos representar, además de colas, también pilas. Investiga cuál es la 
diferencia entre una cola (queue) y una pila (stack). ¿Cómo cambiarían las funciones 
anteriores si en lugar de atender una cola, atendieran una pila?
"""
# RESPUESTA:

""" 
La principal diferencia entre una cola y una pila es el orden en el que se procesan los elementos. En una cola, los elementos se procesan en orden FIFO 
(first in, first out), es decir, el primer elemento en entrar es el primero en salir. En una pila, los elementos se procesan en orden LIFO (last in, first out), 
es decir, el último elemento en entrar es el primero en salir.

En el caso de las funciones anteriores, la diferencia entre atender una cola o una pila se reflejaría en el método de la lista que se utiliza para acceder a 
los elementos. Para atender una cola, se utilizaría el método pop(0), que elimina el primer elemento de la lista. Para atender una pila, se utilizaría el método 
pop(), que elimina el último elemento de la lista.
"""

