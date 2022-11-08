from Producto import Producto

class Detalle:
    def __init__(self,producto:Producto,cantidad,total):
        self._producto=producto
        self._cantidad=cantidad
        self._total=total