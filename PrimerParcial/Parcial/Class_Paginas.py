
class Paginas():
    def __init__(self):
        self.pagina=''
        self.encabezado=''
        self.cuerpo=''
        self.pie_pagina=''
        self.cont=0


    def encabezados(self):
        self.documento=open("pagina.txt","r")
        self.fin=self.documento.readlines()
        self.documento.close()
        for line in self.fin:
            if line == 'Pagina '+str(self.cont+1)+'\n':
                self.cont=self.cont+1
        self.cont=self.cont+1
        self.pagina=open('pagina.txt','a')
        self.encabezado=str(input("Ingrese el encabezado: "))
        self.pagina.write('\n'+'\n'+"Pagina "+str(self.cont)+'\n'+self.encabezado)
        self.pagina.close()

    def cuerpos(self):
        self.pagina=open('pagina.txt','a')
        self.cuerpo=str(input("Ingrese el parrafo: "))
        self.pagina.write('\n'+'\n'+self.cuerpo + '\n')
        fin=str(input("Desea ingresar otro parrafo? si/no\n"))
        while(fin == 'si'):
            self.cuerpo = str(input("Ingrese el parrafo: "))
            self.pagina.write(self.cuerpo + '\n')
            fin = str(input("Desea ingresar otro parrafo? si/no"))
        self.pagina.close()

    def pie_de_pagina(self):
        self.pagina=open('pagina.txt','a')
        self.pie_pagina=str(input("Ingrese el pie de pagina: "))
        self.pagina.write('\n'+'\n'+self.pie_pagina)
        self.pagina.close()
