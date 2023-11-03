# PROGRAMA BUCLE FOR:
# EN ESTE PROGRAMA SE SOLICITA AL USUARIO QUE INGRESE LA CANTIDAD DE PREGUNTES Y EL PRECIO DE CADA UNO DE ELLOS PARA 
# PRINTAR UN COSTO TOTAL.

total=0
veces= int(input("¿Cuántos productos sumar?: "))

for i in range (veces):
    
    precio=float(input("Introducir precio:"))
    total=total+precio
    
print(total)
    
    
    
    
    
    
    