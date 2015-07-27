import socket

dip = input("ESCRIBA DIRECCION IP: ")
inicio = int(input("ESCRIBA EL PUERTO INICIAL:"))
final= int(input("ESCRIBA EL PUERTO FINAL:"))

conexion = socket.socket()
for i in range(inicio,final+1):
	try:
		conexion.connect( (dip, i) )
		print ("Puerto : %s Abierto." % i)
	except:
			print ("Puerto : %s Cerrado." % i)
conexion.close()