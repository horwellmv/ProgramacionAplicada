class Producto:
    def __init__(self,codigo,nombre,precio,stock):
        self._codigo=codigo
        self.nombre=nombre
        self._precio=precio
        self._stock=stock
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,nuevoCodigo):
        if nuevoCodigo != "":
            self._codigo=nuevoCodigo
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,nuevoPrecio):
        self._precio=nuevoPrecio
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self,nuevoStock):
        self._stock=nuevoStock
    
    
    def __str__(self):
        return "Producto Codigo:{}, Nombre:{}, Precio:{}, Stock:{}. ".format(
            self.codigo,
            self.nombre,
            self.precio,
            self.stock
        )
    
    def aumentarStock(self,nuevoStock):
        self.stock=nuevoStock
        print("Hemos cambiado el stock")

