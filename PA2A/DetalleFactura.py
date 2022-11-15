from Producto import Producto

from Proveedor import productosList

DetalleList=[]

def newDetalle(nTicket,produc,cant=1):
    for i in productosList:
        if i.producto == produc:            
            if i.stock>=cant:
                i.stock-=cant
                produc=i
                Detalle(nTicket,produc,cant)
            else: print("Metodo NewDetalle: No hay stock suficiente.") 


class Detalle:        
    def __init__(self,ticketDetalle,articulo:Producto,cantidad=1):
        self._ticketDetalle=ticketDetalle
        self._articulo=articulo.producto
        self._cantidad=cantidad
        self._precioU=round(articulo.precio*1.15)  # Agregamos el 15% de valor ganado
        self._total=round(self.precioU*self.cantidad) # Calculamos el total del detalle
        print("DetalleClass: Detalle creado")
        self.guardarDetalle()

    def __str__(self) -> str:
        return "- {} - {} - {} - {} - {} ".format(
            self.ticketDetalle,
            self.articulo,
            self.cantidad,
            self.precioU,
            self.total
            )

    def guardarDetalle(self):
        DetalleList.append(self)

    # ----------------------------  Getters & Setters
    @property
    def articulo(self):
        return self._articulo
    
    @property
    def ticketDetalle(self):
        return self._ticketDetalle

    @property
    def precioU(self):
        return self._precioU

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self,newCantidad):
        self._cantidad=newCantidad
    
    @property
    def total(self):
        return self._total
