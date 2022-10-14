from Producto import Producto


class Comestible(Producto):
    def __init__(self, codigo, nombre, precio, stock, fechaVencimiento):
        super().__init__(codigo, nombre, precio, stock)
        self._fechaVencimiento=fechaVencimiento
    
    @property
    def fechaVencimiento(self):
        return self._fechaVencimiento
    
    @fechaVencimiento.setter
    def fechaVencimiento(self, nuevaFecha):
        self._fechaVencimiento=nuevaFecha
    
    def __str__(self):
        return super().__str__() + " Fecha de Vencimiento: {}.".format(self.fechaVencimiento)
    
