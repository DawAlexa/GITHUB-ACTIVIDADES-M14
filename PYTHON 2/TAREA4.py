"""
TAREA 4 (1.5 puntos). Utiliza una lista para representar una cola de pedidos en un almacén: 
cola_pedidos = [pedido345671, pedido628316, pedido235252, ...] 
Programa tres funciones: 
(NOTA: usa los métodos propios de las listas: pop, append...)
"""
cola_pedidos = [345671, 628316, 235252] 

"""
a)Una función procesarPedido que saque el primer pedido de la cola y lo muestre por 
pantalla. Ej: “Procesando pedido345671....”
"""
def procesarPedido(cola_pedidos):
    # Sacamos el primer pedido de la cola
    pedido = cola_pedidos.pop(0)

    # Mostramos el pedido por pantalla
    print("Procesando pedido", pedido, "...")

    return pedido


"""
b)Una función encolarPedido que añada un pedido al final de la lista. 
"""
# def encolarPedido(cola_pedidos, pedido):
#     # Añadimos el pedido al final de la cola
#     cola_pedidos.append(pedido)

#     return cola_pedidos


"""
c)Una función vaciarCola que elimine todos los pedidos de la lista. 
"""
# def vaciarCola(cola_pedidos):
#     # Eliminamos todos los pedidos de la cola
#     while len(cola_pedidos) > 0:
#         cola_pedidos.pop(0)

#     return cola_pedidos


"""
d)Con listas podemos representar, además de colas, también pilas. Investiga cuál es la 
diferencia entre una cola (queue) y una pila (stack). ¿Cómo cambiarían las funciones 
anteriores si en lugar de atender una cola, atendieran una pila?
"""
# RESPUESTA: Las funciones encolarPedido y vaciarCola no necesitarían ningún cambio si atendieran una pila.

# def procesarPedido(pila_pedidos):
#     # Sacamos el último pedido de la pila
#     pedido = pila_pedidos.pop()

#     # Mostramos el pedido por pantalla
#     print("Procesando pedido", pedido, "...")

#     return pedido
