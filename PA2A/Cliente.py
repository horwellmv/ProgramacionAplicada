from Persona import Persona

class Cliente(Persona):
    def __init__(self, dni, esSocio, descuento=0) :
        super().__init__()
        self._dni=dni
        self._esSocio=esSocio
        self._descuento=descuento
    
# ------------------------------ Metodos de clase

    def __init__(self):
        super().__init__() + " Dni: {} - Desc: {}%. ".format(
            self.dni,
            self.descuento
        )

# ---------------------------- Getters and Setters

    @property
    def id(self):
        return self._id
    
    @property
    def esSocio(self):
        return self._esSocio
    
    @esSocio.setter
    def esSocio(self, estado):
        self._esSocio=estado
    
    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, nuevoDescuento):
        self._descuento=nuevoDescuento

