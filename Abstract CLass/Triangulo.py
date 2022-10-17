from AbstractClass import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)
    
    def __str__(self) -> str:
        return "Triangulo de Alto: {} y Base: {}.".format(self.alto, self.ancho)
    
    def calcularArea(self):
        return self.alto*self.ancho/2

#test
tri1 = Triangulo(5,10)
print(tri1)
print(tri1.calcularArea())

