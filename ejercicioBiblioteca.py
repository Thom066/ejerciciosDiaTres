
biblioteca={}

def crearLibro():
    print("HOla VAS a CREAR UN LIBRO")

    id=input("Ingrese Id Del Libro-->")

    titulo=input("INgrese Titulo-->")

    autor=input("Ingrese Autor-->")

    year=input("Ingrese Año-->")

    print("---"*10)

    biblioteca[id]={
        "titulo":titulo,
        "autor":autor,
        "año":year
    }
    print("Libro Creado Con Exito")
    print("---"*10)


def verLibro():
    print("---"*10)
    print(biblioteca)
    print("---"*10)


def actualizarLibro():

    print("Actualizar Libro")
    print(biblioteca)
    print("QUE DESEAS ACTUALIZAR:\n 1)titulo\n 2)autor\n 3)año")
    opciones = input("Ingrese Una Opcion--->")

    if opciones == "1":
        id1=input("Ingrese el id del libro-->")
        libroen=biblioteca[id1]
        print(libroen)

        if id1 in biblioteca:
            print("si se encuntra en la biblioteca")
            nuevo_titulo=input("ingresa el nuevo titulo: ")
            libroen['titulo']=nuevo_titulo
            print(libroen)
           
        else:
            print("este id no se encuentra en la biblioteca") 

    elif opciones =="2":
        print("Ingreso autor ")
        id1= input("Ingrese el id del libro-->")
        libroen = biblioteca[id1]
        print(libroen)

        if id1 in biblioteca:
            print("si se encuentra en la biblioteca")
            autor_nuevo = input("INgrese el nuevo autor: ")
            libroen['autor'] =autor_nuevo
            print(libroen)

        else :
            print("este id no se encuentra")


    elif opciones =="3":
        print("Ingreso al año")
        id1 = input ("Ingrese el id: ")
        libroen = biblioteca[id1]
        print(libroen)

        if id1 in biblioteca:
            print("Este libro se encuentra en la biblioteca")
            anio_nuevo= input("Ingrese el nuevo año: ")
            libroen['year'] = anio_nuevo
            print(libroen)

        else:
            print("Este id no se encuentra")

    else :
        print("Opcion invalida")

def eliminar():
    print("Eliminar libro")
    print(biblioteca)
    eliminar_libro = input("Ingresa el id del libro que quieres eliminar: ")
    if biblioteca.pop(eliminar_libro,None):
          print("Libro eliminado con exito")
    else :
       print("No es valido")



while True:
    print("1)Crear Libro  \n 2)Ver Libros \n " \
    "3)Actualizar Libro \n 4)Elimiar Libro \n 5)Salir")

    opcion=input("Ingrese Una Opcion--->")

    if opcion =="1":
        crearLibro()
    elif opcion=="2":
        verLibro()
        
    elif opcion=="3":
        actualizarLibro()

    elif opcion=="4":
        eliminar()
    
    elif opcion=="5":
        break
    
    else:
        print("opcion invalida")
