
from Producto import *


class ProductoConsumo(Producto):
    def __init__(self, producto, stock: int, categoria, precio: int, vencimiento):
        super().__init__(producto, stock, categoria, precio)
        self._vencimiento=vencimiento
        self.guardar()
    
    def __str__(self) -> str:
        return super().__str__()+" - {}".format(self.vencimiento)
    
    # -------------------- Getters & Setters

    @property
    def vencimiento(self):
        return self._vencimiento
    
    @vencimiento.setter
    def vencimiento(self, newVencimiento):
        self._vencimiento=newVencimiento
    
    # ------------------------- Metodos de la clase

    def actualizarVencimiento(self,newVencimiento):
        self.vencimiento=newVencimiento
        return "\n-- Vencimiento actualizado --\n"
    
