"""
TAREA 1 (2 puntos). 
"""


""" a)Crea una variable tableroAjedrez, que sea una lista de de 6 elementos. 
 Cada elemento deberá ser, a su vez, una lista de 6 elementos. """

tableroAjedrez = [[(),(),(),(),(),(),()],
                  [(),(),(),(),(),(),()],
                  [(),(),(),(),(),(),()],
                  [(),(),(),(),(),(),()],
                  [(),(),(),(),(),(),()],
                  [(),(),(),(),(),(),()]]

""" b)Asigna a tableroAjedrez las posiciones de las fichas de ajedrez al inicio de partida. Cada 
 ficha se representará por una tupla de dos string: (ficha,color). Por ejemplo, el caballo negro 
 se representará por (‘C’,’N’). (El resto de códigos de ficha serán: ‘P’ (peón), ‘T’ (torre), ‘A’ (alfil), ‘K’ (rey), ‘Q’ (reina)). """

tableroAjedrez[0][0] = ("T", "N")
tableroAjedrez[0][1] = ("C", "N")
tableroAjedrez[0][2] = ("A", "N")
tableroAjedrez[0][3] = ("Q", "N")
tableroAjedrez[0][4] = ("K", "N")
tableroAjedrez[0][5] = ("A", "N")
tableroAjedrez[0][6] = ("C", "N")
tableroAjedrez[1][0] = ("P", "N")
tableroAjedrez[1][1] = ("P", "N")
tableroAjedrez[1][2] = ("P", "N")
tableroAjedrez[1][3] = ("P", "N")
tableroAjedrez[1][4] = ("P", "N")
tableroAjedrez[1][5] = ("P", "N")
tableroAjedrez[1][6] = ("P", "N")
tableroAjedrez[2][0] = ("")
tableroAjedrez[2][1] = ("")
tableroAjedrez[2][2] = ("")
tableroAjedrez[2][3] = ("")
tableroAjedrez[2][4] = ("")
tableroAjedrez[2][5] = ("")
tableroAjedrez[2][6] = ("")
tableroAjedrez[3][0] = ("P", "B")
tableroAjedrez[3][1] = ("P", "B")
tableroAjedrez[3][2] = ("P", "B")
tableroAjedrez[3][3] = ("P", "B")
tableroAjedrez[3][4] = ("P", "B")
tableroAjedrez[3][5] = ("P", "B")
tableroAjedrez[3][6] = ("P", "B")
tableroAjedrez[4][0] = ("C", "B")
tableroAjedrez[4][1] = ("A", "B")
tableroAjedrez[4][2] = ("T", "B")
tableroAjedrez[4][3] = ("Q", "B")
tableroAjedrez[4][4] = ("K", "B")
tableroAjedrez[4][5] = ("A", "B")
tableroAjedrez[4][6] = ("C", "B")

""" c)Define una función moverCaballo(color, posicion) a la que se le pase el color del caballo 
 que se pretende mover y la posición a la que se quiera mover la ficha, ambos como string. 
 Por ejemplo: moverCaballo(‘N’,‘3A’).
 La función debe evaluar si el movimiento deseado está permitido. En caso afirmativo, 
 actualizará la posición del tablero y retornará True. En caso negativo, retornará False. """


def moverCaballo(color, posicion):

    # Comprobamos que la posición esté vacía

    if tableroAjedrez[posicion[0]][posicion[1]] != (""):
        return False

    # Obtenemos las coordenadas del caballo

    caballo = tableroAjedrez[posicion[0]][posicion[1]]
    caballoX = posicion[0]
    caballoY = posicion[1]

    # Comprobamos si el movimiento es válido

    if (abs(caballoX - posicion[0]) == 2 and abs(caballoY - posicion[1]) == 1) or (
        abs(caballoX - posicion[0]) == 1 and abs(caballoY - posicion[1]) == 2
    ):
        # Actualizamos la posición del caballo

        tableroAjedrez[posicion[0]][posicion[1]] = caballo
        tableroAjedrez[caballoX][caballoY] = ("")
        return True
    else:
        return False


""" d)Partiendo de la posición inicial del tablero, mover el caballo blanco a C3, y luego a D4. """


# if moverCaballo("B", "C3"):
#     print("El caballo blanco se ha movido a C3")

# elif moverCaballo("B", "D4"):
#     print("El caballo blanco se ha movido a D4")

# else:
#     print("El movimiento no es válido")


print(tableroAjedrez)
