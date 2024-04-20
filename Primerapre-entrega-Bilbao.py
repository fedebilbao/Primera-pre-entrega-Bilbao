""" VARIABLES """

nombre = ""
contraseña = ""
lista_usuarios=[]
diccionario_usuarios= {}
i=0

""" FUNCIONES """

def guardar_datos (usuario, contraseña):
    Diccionario_Usuarios = {Usuario: Contraseña,}
    Lista_Usuarios.append(Diccionario_Usuarios)
def mostrar_datos ():
    print (lista_usuarios)
def login(i):

    while i==0:

        usuario = input ("Usuario:")
        contraseña = input ("Contraseña:")
        if {usuario:contraseña} in lista_usuarios:
            print ("Usted ingresó correctamente")
            i=1

        else:
            print ("Los datos no fueron cargados correctamente o usted no posee una cuenta")

""" PROGRAMA """

print ("BIENVENIDO A NUESTRO SISTEMA")

while i==0:
    estado = str (input ("Si sos nuevo en la plataforma escribí SI en caso contrario si queres ingresar a tu cuenta escribí NO: "))
    estado = estado.upper()

    """ print (Estado) """

    if estado == "SI":
        usuario = input ("Usuario: ")
        contraseña = input ("Contraseña: ") 
        guardar_datos(usuario, contraseña)
        print (lista_usuarios)

    elif estado == "NO":
        login(i)

    i= int(input("si queres volver al menú principal presioná 0, si queres finalizar presiona cualquier otro número: "))

else: 
    print("Muchas gracias por usar nuestra plataforma")

    

