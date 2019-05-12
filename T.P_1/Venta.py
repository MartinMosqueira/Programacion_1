from Class_TarjetaCredito import TarjetaCredito

class Venta():

    def __init__(self):
        self.monto=0
        self.descripcion=''
        TarjetaCredito
        self.archive=''
        self.cadena=''


    def show1(self):
        self.monto=int(input("Monto: "))
        self.descripcion=str(input("Descripcion: "))
        self.cadena=str(TarjetaCredito().show())+' Monto: '+str(self.monto)+' Descripcion: '+self.descripcion
        self.archive=open('Card.json','a')
        self.archive.write(self.cadena)
        self.archive.close()