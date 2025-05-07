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
    print (agendaContactos[buscar])
    if buscar in agendaContactos:
        print("---"*10)
        print("Contacto encontrado")
        print(agendaContactos)
    else :
        print("El contacto no existe")

    


while True:
    print("1) Crear contacto \n 2) Ver contactos \n 3) Buscar contactos \n 4) Actualizar contactos \n 5) Eliminar contactos \n 6) salir")

    opcion = input ("Ingrese una opcion--->")

    if opcion == "1":
        crearContacto()
    elif opcion == "2":
        verContactos()
    elif opcion == "3":
        buscarContactos()