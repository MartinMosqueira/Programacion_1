import shutil
import os

class EmptyFileExcetion(Exception):
    pass


class Selection_Archive():

    def __init__(self,archives,archivess):
        self.archives=archives
        self.archivess=archivess
        self.diccionary={}

    def exercice1(self):
        self.archives = open('archive.txt', "r")
        for line in self.archives:
            print(line)
        self.archives.close()

    def exercice2(self):
        self.archives = open('archive.txt','r')
        for l in self.archives:
            print("Nombre: ",l.split()[0])
            print("Apellido: ",l.split()[1])
            print("Monto: ",l.split()[2])
            print("Descripcion: ",l.split()[3])
            print("Pago: ",l.split()[4])
        self.archives.close()

    def exercice3(self):
        self.archives = open('archive.txt','r')
        self.archivess = open('ARCHIVO_ORIGINAL.json','w')
        os.rename('archive.txt','archive.json')

        for l in self.archives:
            key=l.split()
            self.diccionary['Nombre']=key[0]
            self.diccionary['Apellido']=key[1]
            self.diccionary['Costo']=key[2]
            self.diccionary['Descripcion']=key[3]
            self.diccionary['Pago']=key[4]
            print(self.diccionary)

        shutil.copyfileobj(self.archives, self.archivess)
        self.archives.close()
        self.archivess.close()

    def exercice4(self):
        self.archives = open('archive.json','r')
        content=self.archives.read()
        if content == '':
            print('Ocurrió un problema con la fuente de datos...')
            raise EmptyFileExcetion
        else:
            print(content)
