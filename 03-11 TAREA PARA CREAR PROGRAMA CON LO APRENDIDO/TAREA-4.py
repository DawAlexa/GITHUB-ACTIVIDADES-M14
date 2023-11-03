# PROGRAMA USANDO IF-ELSE ANIDADO: 
# ALESHOP OFRECE DESCUENTOS EN SUS PRODUCTOS, DEPENDIENDO DEL PRECIO SE LE ASIGNA UN DETERMINADO DESCEUNTO, ENTONCES SOLICITAR AL USUARIO
# INGRESAR EL PRECIO DEL PRODUCTO Y PRINTAR SU DESCUENTO.

print("¡Bienvenido a ALESHOP! Reclama tu cupón.")
producto= float(input("Ingresa precio del producto: "))

if producto<=20:
    print("El precio del producto no aplica a un descuento")

elif producto <= 50 :
    calculo1= producto-(producto*0.05)
    print("tu descuento es del 5% y el precio final es",  calculo1)

elif producto <=100:
    calculo2= producto-(producto*0.10)
    print("tu descuento es del 10% y el precio final es",  calculo2)

elif producto >=100:
    calculo3= producto-(producto*0.15)
    print("tu descuento es del 15% y el precio final es",  calculo3)

else:
    print("Descuento no disponible")
    
    
    
    
    