class Cliente ():
    def __init__(self, nombre, apellido, dni, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

    def __str__(self):
        return f"Hola, {self.nombre} {self.apellido}, usted ha creado su usuario de forma exitosa y su mail al que le llegará la factura de su compra es: {self.mail}"

    def agregar_al_carrito(self, producto, cantidad):
        print (f"usted agregó {cantidad} {producto} al carrito")

    def modificar_mail(self):
        newmail =input ("Escriba su nuevo mail:")
        self.mail = newmail
        print (f"Usted modificó correctamente su mail y ahora es {self.mail}")


        

    