from Persona import Persona

class Proveedor(Persona):
    def __init__(self, cuit, razonSocial, categoria):
        super().__init__()
        self._cuit=cuit
        self._razonSocial=razonSocial
        self._categoria=categoria
    

# ----------------------------- Metodos de la clase

    def __init__(self):
        super().__init__() + " Razon Social: {} - Cuit: {} - Categoria: {}.".format(
            self.razonSocial,
            self.cuit,
            self.categoria
        )

# ----------------------------- Getters & setters

    @property
    def cuit(self):
        return self._cuit

    @property
    def razonSocial(self):
        return self._razonSocial
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,nuevaCategoria):
        self._categoria=nuevaCategoria