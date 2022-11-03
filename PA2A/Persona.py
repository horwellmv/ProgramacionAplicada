#Clase abtracta - Hay que importar la clase abc y la clase @abtsractclassmethod

from abc import ABC, abstractclassmethod

class Persona(ABC):
    def __init__(self,nombre,id,telefono,direccion):
        self._nombre=nombre
        self._telefono=telefono
        self._direccion=direccion
    

    # ---------------------------------- Meotodos Abstr

    def __init__(self):
        return "Nombre: {} - Telefono: {} - Direccion: {} -".format(
            self.nombre,
            self.telefono,
            self.direccion
        )

    @abstractclassmethod
    def metodo():
        pass


    # --------------------------------- Getters & Setters

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self,nuevoTelefono):
        self._telefono=nuevoTelefono

    @nombre.setter
    def nombre(self, nuevaFecha):
        self._fechaVencimiento=nuevaFecha
    
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self,nuevaDireccion):
        self._direccion=nuevaDireccion

