# ------------------------------ TEST
from ProductoConsumo import ProductoConsumo # Eliminar, era solo para test
from Cliente import *
from ProductoLimpieza import *
from DetalleFactura import *
from Factura import *


cli1=Cliente(1,"Horwell",10)
cli2=Cliente(2,"Gigi",5)


pr1=ProductoConsumo("coca",10,"PC",100,"marzo")
pr2=ProductoConsumo("coco",10,"PC",200,"marzo")
pr3=ProductoConsumo("cacao",10,"PC",500,"marzo")
pr4=ProductoLimpieza("trapo",10,"PL",10,"lote1")

newDetalle(1,"coca",2)
newDetalle(1,"coco",8)
newDetalle(1,"cacao",5)

print("Productos de tienda:--------------------- ")

for i in productosList:
    print ( i)

print(" Productos para la factura  ----------")

for i in DetalleList:
    print(i)

print(" Esta es la factura y sus datos ----------")

fact1=Factura(1,1)
print(fact1)