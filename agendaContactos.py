agendaContactos={}

def crearContacto():
    
    print("Crear nuevo contacto")

    nombre = input("Ingresa el nombre: ")

    telefono = input("Ingresa el numero: ")
    
    correo = input("Ingresa el correo: ")
    
    print("---"*10)

    agendaContactos[nombre]={
    'telefono': telefono,
    'correo' : correo
    }
    print("Creaste un contacto")

    print("---"*10)

def verContactos():

    print("---"*10)

    print("Viendo contactos")
    print(agendaContactos)

    print("---"*10)

def buscarContactos():
    buscar = input("Digita el nombre: ")
    print("---" * 10)

    contacto = agendaContactos.get(buscar)

    if contacto:
        print("Contacto encontrado")
        print("---" * 10)
        print("Nombre:",buscar)
        print("Telefono: ", contacto["telefono"])
        print("Correo: ", contacto["correo"])
    else :
        print("El contacto no existe")

    print("---"*10)


#falta terminar la funcion de actualizar los contactos
def actualizarContactos():
    print("---"*10)
    print("Entraste a actualizar contactos")
    print("---"*10)
    print(agendaContactos)
    nom1 = input("Que contacto deseas actualizar: ")

def eliminarContactos():
    print("Eliminar contactos")
    print(agendaContactos)

    while True:
        contactoElim = input("Ingresa el nombre del contacto que deeas eliminar: ")

        if contactoElim not in agendaContactos:
            print("Este contacto no se encuentra. Ingrese bien el nombre")
        else:
            agendaContactos.pop(contactoElim)
            print("Contacto eliminado con exito")
            break



while True:
    print("1) Crear contacto \n 2) Ver contactos \n 3) Buscar contactos \n 4) Actualizar contactos \n 5) Eliminar contactos \n 6) salir")

    opcion = input ("Ingrese una opcion--->")

    if opcion == "1":
        crearContacto()
    elif opcion == "2":
        verContactos()
    elif opcion == "3":
        buscarContactos()
    elif opcion == "4":
        actualizarContactos()
    elif opcion == "5":
        eliminarContactos()
    elif opcion == "6":
        break
    else:
        print("opcion invalida")
