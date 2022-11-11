
from Producto import *


class ProductoLimpieza(Producto):
    def __init__(self, producto, stock: int, categoria, precio: int, lote):
        super().__init__(producto, stock, categoria, precio)
        self._lote=lote
        self.guardar()
    
    def __str__(self) -> str:
        return super().__str__()+" - {}".format(self.lote)
    
    # -------------------- Getters & Setters

    @property
    def lote(self):
        return self._lote
    
    @lote.setter
    def lote(self, newLote):
        self._lote=newLote
    
    # ------------------------- Metodos de la clase

    def actualizarLote(self,newLote):
        self.lote=newLote
        return "\n-- Lote actualizado --\n"
    
