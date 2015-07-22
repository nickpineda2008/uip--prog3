import os
print ("Supermercado ABC")
lista = []
opcion=0
contador = 0
while opcion != "4":
		print("1. Agregar un objeto")
		print("2. Eliminar un objeto")
		print("3. Ver su lista")
		print("4. Salir")
		
		opcion = input("Selecione una opcion: ")
		
		if opcion == "1":
				objeto=input("Escriba el objeto a agregar: ")
				contador = contador + 1
				objeto = (str(contador)+"- "+ str (objeto))
				lista.append(objeto)
		if opcion == "2":
				print(lista)
				eliminar= int(input("Seleccione el objeto a eliminar: "))
				print(lista[eliminar]+" Fue eliminado")
				del lista [eliminar]
		if opcion == "3":
				print(lista)
input()