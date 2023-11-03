# PROGRAMA USANDO IF-ELSE BÁSICO: 
# EL USUARIO DESEA SABER QUE TIPO DE PC PUEDE COMPRAR CON SU PRESUPUESTO.


print("INTRODUCE TU PRESUPUESTO PARA SABER QUE PC PUEDES COMPRAR")

presupuesto= int(input("Ingresar presupuesto: "))

if presupuesto<=1000:
    print("Puedes comprar una pc de bajo y medio recursos para funciones de oficina o estudiante")

else:
    print("Puedes comprar una pc de altos recursos para funciones gamer o diseñador")


