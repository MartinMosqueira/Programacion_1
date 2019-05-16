from Class_Documento import Documento

documento=Documento()
respuesta=str(input("1:Ingresar un nuevo documento"+'\n'+"2:Recuperar un documento"+'\n'"Respuesta:"))
if respuesta == str(1):
    print(documento.agregar_pagina())
    print(documento.mostrar())
else:
    print(documento.recuperar_archivo())
    print(documento.mostrar())

#print(documento.eliminar_pagina())