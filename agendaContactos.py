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


def actualizarContactos():
    print("Entraste a actualizar contactos")
    print(agendaContactos)
    print("Que desea actualizar:\n 1)telefono\n 2)correo\n")

    #while True:
    opcionesActualizar = input("Digite la opcion: ")

    if opcionesActualizar=="1":
        contacAct= input("Que contacto deseas actualizar: ")
        contacEncont=agendaContactos[contacAct]
        print(contacEncont)

        while True:

            if contacAct  not in agendaContactos:
                print("Este contacto no se encuentra en la agenda. Digita el nombre otra vez")
        
            else:
                print ("Este contacto esta en la agenda")
                nuevoTelefono = input("Ingresa el nuevo numero: ")
                contacEncont['telefono']=nuevoTelefono
                print(agendaContactos)
                print("Actualizaste el numero")
                break

    elif opcionesActualizar=="2":
        contacAct= input("Que contacto deseas actualizar: ")
        contacEncont=agendaContactos[contacAct]
        print(contacEncont)

        while True:

            if contacAct  not in agendaContactos:
                print("Este contacto no se encuentra en la agenda. Digita el nombre otra vez")
        
            else:
                print ("Este contacto esta en la agenda")
                nuevoCorreo = input("Ingresa el nuevo correo: ")
                contacEncont['correo']=nuevoCorreo
                print("Actualizaste el correo")
                print(agendaContactos)
                break
        
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
