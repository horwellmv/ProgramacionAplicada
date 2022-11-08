#Clase abtracta - Hay que importar la clase abc y la clase @abtsractclassmethod

from abc import ABC, abstractclassmethod

class Persona(ABC):
    def __init__(self,telefono="Null",direccion="Null"):
        self._telefono=telefono
        self._direccion=direccion
    
        # ---------------------------------- Metodos Abstr

    @abstractclassmethod
    def guardar():
        pass

    @abstractclassmethod
    def editar():
        pass

        # --------------------------------- Getters & Setters

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self,nuevoTelefono):
        self._telefono=nuevoTelefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self,nuevaDireccion):
        self._direccion=nuevaDireccion

