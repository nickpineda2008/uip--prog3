import Libro, Copia, Lector, Autor
print ("Menu")
lista1 = []
lista2 = []
lista3 = [] 
opcion = 0
_estado = 10
while opcion < "6":
		print("1. INTRODUCIR UN LECTOR")
		print("2. INTRODUCIR UN AUTOR")
		print("3. INTRODUCIR UN LIBRO")
		print("4. HACER PETICION")
		print("5. HACER DEVOLUCION")
		
		opcion = int(input("Selecione una opcion: "))
		
		if opcion == "1":
		nombre=input("Escriba el nombre del lector: ")
		id=input("Escriba la identificacion del lector: ")
		lec = Lector.Lector(nombre,id)
		lista1.append(lec)
		
		if opcion == "2":
		nombre=input("Escriba el nombre del Autor: ")
		nacionalidad=input("Escriba la nacionalidad del Autor: ")
		nac = Autor.Autor(nombre,nacionalidad)
		lista2.append(nac)
		
		if opcion == "3":
		titulo=input("Escriba el titulo del Libro: ")
		tipo=input("Escriba el tipo de Autor: ")
		editorial=imput("Escriba la editorial del libro: ")
		lib = Libro.Libro(titulo,tipo,editorial)
		lista3.append(lib)
		
		if opcion =="4":
		print("HACIENDO PETICION")
		cop = Copia.Copia(_id,_estado)
		_estado	== -1
		
		if opcion == "5":
		print("HACIENDO DEVOLUCION")
		_estado == +1
		