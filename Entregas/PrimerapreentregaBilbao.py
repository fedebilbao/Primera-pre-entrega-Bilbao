""" VARIABLES """

user = ""
password = ""
user_list=[]
user_dictionary= {}
i=0

""" FUNCIONES """

def guardar_datos (user, password, lista):
    user_dictionary = {user: password,}
    lista.append(user_dictionary)
def mostrar_datos (lista):
    print (lista)
def login(lista):
    i=0
    while i==0:

        user = input ("Usuario:")
        password = input ("password:")
        if {user:password} in lista:
            print ("Usted ingresó correctamente")
            i=1

        else:
            print ("Credenciales Incorrectas")

""" PROGRAMA """

print ("BIENVENIDO A NUESTRO SISTEMA")

while i==0:
    status = str (input ("Si sos nuevo en la plataforma escribí SI en caso contrario si queres ingresar a tu cuenta escribí NO: "))
    status = status.upper()

    """ print (status) """

    if status == "SI":
        user = input ("Usuario: ")
        password = input ("password: ") 
        guardar_datos(user, password, user_list)
        print (user_list)

    elif status == "NO":
        login(user_list)

    i= int(input("si queres volver al menú principal presioná 0, si queres finalizar presiona cualquier otro número: "))

else: 
    print("Muchas gracias por usar nuestra plataforma")

    

