print (" Calculo de comision ")
print (" Ingrese su nombre y ventas" )
nombre = input ("Nombre: ")
v1 = float (input ("Venta Numero 1: "))
v2 = float (input ("Venta Numero 2: "))
v3 = float (input ("Venta Numero 3: "))
tv = v1+v2+v3
c = tv * 0.125
tvc = tv+c
print (nombre)
print ("El total de las ventas fueron:" + str(tv))
print ("El total de las comisiones fueron" + str (c))
print ("El total de las ventas mas comisiones fueron" + str (tvc))
input()

