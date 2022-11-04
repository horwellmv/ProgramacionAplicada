from Cliente import *

cl1=Cliente(1,"horwell")

cl2=Cliente(2,"gigi",True,20)

for i in clienteList:
    print(i)
    print(" -----------\n")

editarCliente(2,"Gigi",True,35,115050,"Monserrat")

for i in clienteList:
    print(i)
    print(" -----------\n")
