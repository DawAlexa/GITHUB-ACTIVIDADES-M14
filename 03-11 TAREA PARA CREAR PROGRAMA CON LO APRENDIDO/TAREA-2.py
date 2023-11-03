# PROGRAMA USANDO WHILE: 
# PREGUNTAR AL USUARIO, SI DESEA SEGUIR COMPRANDO CADA VER QUE AGREGUE UN ARTICULO AL CARRITO DE COMPRAS Y CUANDO DIGA QUE NO
# MOSTRAR EL TOTAL DE LOS PRODUCTOS

producto=0
print("Estas comprando en ALESHOP")

while True:
    agregar=int(input("¿Añadir articulo? 1-Si 0-No "))
    
    if agregar: 
        producto += 1
    else:
        break
print("En el carrito hay", producto, "productos")

# Puedo salir deL bucle con break o escribiendo directamente el resultado: print("En el carrito hay", producto, "productos")


    


    
    