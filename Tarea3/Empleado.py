from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, fechaNacimiento,legajo,cargo):
        super().__init__(nombre, edad, fechaNacimiento)
        self._legajo=legajo
        self._cargo=cargo
    
    def __str__(self):
        return super().__str__() + " Legajo: {}, Cargo: {}".format(
            self.legajo,
            self.cargo
        )
    
    @property
    def legajo(self):
        return self._legajo

    @property
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self,nuevoCargo):
        self._cargo=nuevoCargo
    
    def modificarCargo(self,nuevoCargo):
        self.cargo=nuevoCargo
    