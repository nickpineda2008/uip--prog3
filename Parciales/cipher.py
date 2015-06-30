import os
print ("Programa de cifrado")
opcion = 0
menu=[]
d=""
while opcion != "4" :
		print ("1 agregar texto")
		print ("2 cifrar texto")
		print ("3 descifrar texto")
		print ("4 imprimirlo en pantalla")
		
		opcion = input ("elija una opcion: ")
		
		if opcion == "1" :
			texto = input ("agrege el texto: ")
		if opcion == "2" :
			for letra in (texto) :
				a=ord(letra)
				b=a+1
				c=chr(b)
				d=c+d
			print ("su texto cifrado es :",d)
				
input ()
				
			
			
			
		