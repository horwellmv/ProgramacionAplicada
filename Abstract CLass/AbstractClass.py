#Clase abtracta - Hay que importar la clase abc y la clase @abtsractclassmethod

from abc import ABC, abstractclassmethod

class FiguraGeometrica(ABC):
    def __init__(self,alto,ancho):
        self.alto=alto
        self.ancho=ancho
    
    @abstractclassmethod
    def calcularArea():
        pass