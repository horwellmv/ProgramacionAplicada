

productosList=[]

class Producto:
    def __init__(self,producto,stock:int,categoria,precio:int):
        self._producto=producto
        self._stock=stock
        self._categoria=categoria
        self._precio=precio
    
    def __str__(self) -> str:
        return "\n- {} - {} - {} - {}".format(
            self.producto,
            self.stock,
            self.categoria,
            self.precio)
    
        # --------------------------- Getters & Setters
    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self,newproducto):
        self._producto=newproducto

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self,newstock):
        self._stock=newstock

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,newcategoria):
        self._categoria=newcategoria

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,newPrecio):
        self._precio=newPrecio

        # --------------------------- Metodos de clase

    def guardar(self):
        productosList.append(self)

    def actualizarStock(self,newStock:int):
        self.stock=newStock
        return "\n-- Stock actualizado --\n"
    
    def actualizarPrecio(self,newPrecio:int):
        self.precio=newPrecio
        return "\n-- Precio Actualizado--\n"


# ----------------------------------- test de clase ------------------------------
