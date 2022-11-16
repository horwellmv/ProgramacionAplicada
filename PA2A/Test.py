# ------------------------------ TEST
from ProductoConsumo import ProductoConsumo # Eliminar, era solo para test
from Cliente import *
from ProductoLimpieza import *
from DetalleFactura import *
from Factura import *


cli1=Cliente(1,"Horwell",10)
cli2=Cliente(2,"Gigi",5)


pr1=ProductoConsumo("aceite",5,"PC",350,"Ago/2023")
pr2=ProductoConsumo("leche",5,"PC",160,"Dic/2022")
pr3=ProductoConsumo("escoba",5,"PL",500,"lote11")
pr4=ProductoLimpieza("secador",5,"PL",300,"lote22")

print("Productos de tienda:--------------------- ")

for i in productosList:
    print ( i)

newDetalle("aceite",5)
newDetalle("leche",5)
newDetalle("escoba",5)

print(" Productos en detalle  ----------")

for i in DetalleList:
    print(i)

print("Agregamos Productos de tienda:--------------------- ")
pr1=ProductoConsumo("aceite",20,"PC",350,"Ago/2023")
pr2=ProductoConsumo("leche",20,"PC",160,"Dic/2022")
pr3=ProductoConsumo("escoba",20,"PL",500,"lote11")
pr4=ProductoLimpieza("secador",20,"PL",300,"lote22")

for i in productosList:
    print ( i)


print(" Esta es la factura y sus datos ----------")

fact1=Factura(90000,1)
print(fact1)


#Resolver: Editar proveedor, editar cliente / 
# Remito no agrega stock, solo crea mas productos iguales / 
# Detalle deberia restar stock al facturar recien / 
# falta funcion cancelar venta / 
# buscar limpiar los campos al cancelar o facturar