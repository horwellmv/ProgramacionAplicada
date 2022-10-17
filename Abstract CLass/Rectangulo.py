from AbstractClass import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)
    
    def __str__(self) -> str:
        return "Rectangulo de Alto: {} y Ancho: {}.".format(self.alto, self.ancho)
    
    def calcularArea(self):
        return self.alto*self.ancho

#test
cua1 = Rectangulo(10,20)
print(cua1.calcularArea())
print(cua1)