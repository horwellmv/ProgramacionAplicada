
class Persona:
    def __init__(self,nombre,edad,fechaNacimiento) :
        self._nombre=nombre
        self._edad=edad
        self._fechaNacimiento=fechaNacimiento
    
    def __str__(self):
        return "Persona Nombre: {}, Edad: {}, Fecha nacimiento: {}.".format(
            self.nombre,
            self.edad,
            self.fechaNacimiento
        )
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre=nuevoNombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,nuevaEdad):
        self._edad=nuevaEdad
    
    @property
    def fechaNacimiento(self):
        return self._fechaNacimiento
    

    


