print("AGENDA DE TELEFONOS")
directorio = {}
opcion = 0
while opcion != 5:
  print("1. VER NUMERO DE TELEFONOS")
  print("2. AGREGAR NUMERO DE TELEFONO")
  print("3. ELIMINAR NUMERO DE TELEFONO")
  print("4. BUSCAR NUMERO DE TELEFONO")
  print("5. SALIR")
  
  opcion =int( input("\nSELECIONE UNA OPCION: "))
  if opcion == 1:
    print("\nDIRECCTORIO DE CONTACTOS\n" + str(directorio)+"\n")
  if opcion == 2:
    nombre = input("INTRODUZCA NOMBRE DEL CONTACTO: ")
    num = int(input("INTRODUZCA EL NUMERO DEL CONTACTO: "))
    directorio[nombre] = num
  if opcion == 3:
    nombre = input("INTRODUZCA EL NOMBRE DEL CONTACTO: ")
    del directorio[nombre]
  if opcion == 4:
    nombre = input("INTRODUZCA EL NOMBRE DE LA PERSONA A LA CUAL DESEA SABER EL NUMERO: ")
    print(str(directorio[nombre]) )

