# USANDO STRINGS
# En un almacen hay paquetes identificados por un código y cada fragmento indica la dimension del paquete.
# La empresa de transporte desea saber las dimensiones calcular el tipo de transporte. Solicitar código y printar la dimensión.

print("Consulta la dimensión del paquete")  

while True:
    codigo=str(input("Introduce el código de 6 digitos ó f para finalizar: "))
    
    if codigo !="f":
        print("El paquete mide", codigo[0:3],"cm","de alto", "y de ancho", codigo[3:6],"cm")
    
    if codigo=="f":
        print("Consulta finalizada")




