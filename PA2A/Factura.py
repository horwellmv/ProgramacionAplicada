from datetime import datetime
from DetalleFactura import *
from Cliente import clienteList

facturaList=[]

class Factura():
    def __init__(self,ticket,dniCliente=0):
        self._fecha=datetime.now()
        self._ticket=ticket
        self.detallesFactura=[]
        self._dniCliente=dniCliente
        self._nombreCliente="No socio."
        self._descuento=0
        self._total=0
        self._precioFinal=0
        self.cargarCliente()
        self.cargarDetalles()
        self.cargarTotal()
        self.cargarDescuento()
        self.cargarFactura()

    def __str__(self) -> str:
        return" Cliente: {} -  Subtotal: ${} - Descuentos:-{}%  -  TOTAL: ${} ".format(self.nombreCliente, self.total, self.descuento, self.precioFinal)

    # Objeto self,ticketDetalle,articulo:Producto,cantidad=1
    def cargarDetalles(self):
        for i in DetalleList:
            if i.ticketDetalle == self.ticket:
                self.detallesFactura.append(i) # En lista con formato (- 1 - coca - 1 - 115 - 115)
                print("FacturaClass: Metodo cargar detalle: detalle facturado")
            else: print("FacturaClass: No se econtraron detalles a facturar")

    #dni:int, nombre, descuento:int=0,telefono="Null",direccion="Null"
    def cargarCliente(self):
        for i in clienteList:
            if i.dni==self.cliente:
                self.descuento=i.descuento
                self.nombreCliente=i.nombre
                print("Metodo CargarCliente: Cliente encontrado.")
            else: print("Metodo CargarCliente: Cliente no encontrado.")
    
    def cargarTotal(self):
        for i in self.detallesFactura:
            self.total+=i.total
        self.precioFinal=self.total
        print("FacturaClass: Metodo cargarTotal ejecutado")
    
    def cargarDescuento(self):
        desc= (self.total*self.descuento)/100
        self.precioFinal-=round(desc)
        print("FacturaClass: Metodo cargarDescuento ejecutado")

    def cargarFactura(self):
        facturaList.append(self)
        print("FacturaClass: Metodo cargarFactura ejecutado")

    # ------------------------- Getters & Setters

    @property
    def ticket(self):
        return self._ticket
    
    @ticket.setter
    def ticket(self,newTicket):
        self._ticket=newTicket
    
    @property
    def cliente(self):
        return self._dniCliente
    
    @cliente.setter
    def dniCliente(self,newCliente):
        self._dniCliente=newCliente
    
    @property
    def nombreCliente(self):
        return self._nombreCliente
    
    @nombreCliente.setter
    def nombreCliente(self,newNombre):
        self._nombreCliente=newNombre

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self,newDescuento):
        self._descuento=newDescuento
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,newTotal):
        self._total=newTotal
    
    @property
    def precioFinal(self):
        return self._precioFinal
    
    @precioFinal.setter
    def precioFinal(self,newPrecioFinal):
        self._precioFinal= newPrecioFinal #-=round(self.total*self.descuento)

