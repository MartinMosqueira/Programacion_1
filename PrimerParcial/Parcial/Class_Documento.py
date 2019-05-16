from Class_Paginas import Paginas

class Documento():
    def __init__(self):
        self.documento=''
        self.pagina=Paginas()
        self.fin=''
        self.cont=1

    def agregar_pagina(self):
        self.documento=open('pagina.txt','w')
        print("Primera pagina..")
        self.pagina.encabezados()
        self.pagina.cuerpos()
        self.pagina.pie_de_pagina()
        self.fin=str(input("Desea ingresar otra pagina? si/no"))
        while(self.fin == 'si'):
            self.cont=self.cont+1
            print("Pagina"+str(self.cont)+"..")
            self.pagina.encabezados()
            self.pagina.cuerpos()
            self.pagina.pie_de_pagina()
            self.fin = str(input("Desea ingresar otra pagina? si/no"))

    def mostrar(self):
        self.documento=open("pagina.txt","r")
        for line in self.documento:
            print(line[:-1])

        self.documento.close()

#la funcion eliminar pagina se me complico bastante por el hecho de no saber como dividir las paginas
    #pude  hacer solo lo que esta en la funcion
    def eliminar_pagina(self):
        self.documento=open('pagina.txt','r')
        self.fin=self.documento.readlines()
        self.documento.close()
        self.documento=open('pagina_new.txt','w')
        for line in self.fin:
            if line != 'Pagina 1'+'\n':
                self.documento.write(line)

    def recuperar_archivo(self):
        self.documento=open("pagina.txt","r")
        self.fin=self.documento.readlines()
        self.documento.close()
        for line in self.fin:
            if line == 'Pagina '+str(self.cont)+'\n':
                self.cont=self.cont+1
        print("El documento contiene "+str(self.cont-1)+" paginas...")
        self.documento=open("pagina.txt","a")
        print("Pagina "+str(self.cont))
        self.pagina.encabezados()
        self.pagina.cuerpos()
        self.pagina.pie_de_pagina()
        self.fin=str(input("Desea ingresar otra pagina? si/no"))
        while(self.fin == 'si'):
            self.cont=self.cont+1
            print("Pagina"+str(self.cont)+"..")
            self.pagina.encabezados()
            self.pagina.cuerpos()
            self.pagina.pie_de_pagina()
            self.fin = str(input("Desea ingresar otra pagina? si/no"))

