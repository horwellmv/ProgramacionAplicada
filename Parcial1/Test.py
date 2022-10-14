from Producto import Producto
from Comestible import Comestible

producto1=Producto(1,"Carro",1.200,4)

print(producto1)
producto1.codigo=2
producto1.precio=321321
producto1.stock=900
print(producto1)
producto1.aumentarStock(1000)
print(producto1)

miComestible = Comestible(2,"Caramelo",300.00,100,"agosto")
print(miComestible)
miComestible.fechaVencimiento="septiembre"
miComestible.aumentarStock(200)
miComestible.precio=400
print(miComestible)