class TarjetaCredito():

    def __init__(self):
        self.nombre=''
        self.apellido=''
        self.numero=0
        self.codigo=0
        self.tipo=''
        self.archive=''
        self.cadena=''

    def show(self):
        print("Ingrese los datos de la tarjeta...")
        self.nombre=str(input("Nombre: "))
        self.apellido=str(input("Apellido: "))
        self.numero=int(input("Numero: "))
        self.codigo=int(input("Codigo: "))
        self.tipo=str(input("Tipo: "))
        self.cadena='Nombre: '+self.nombre+' Apellido: '+self.apellido+' Numero: '+str(self.numero)+' Codigo: '+str(self.codigo)+' Tipo: '+self.tipo
        self.archive=open('Card.json','w')
        self.archive.write(self.cadena)
        self.archive.close()

