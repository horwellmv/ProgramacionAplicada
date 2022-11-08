
class Producto:
    def __init__(self,codigo,nombre,marca,precio,stock):
        self._codigo=codigo
        self._nombre=nombre
        self._marca=marca
        self._precio=precio
        self._stock=stock
        self.guardar()
    
        # --------------------------- Getters & Setters
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self,newCodigo):
        self._codigo=newCodigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,newNombre):
        self._nombre=newNombre

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,newMarca):
        self._marca=newMarca

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,newPrecio):
        self._precio=newPrecio
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self,newStock):
        self._stock=newStock

        # --------------------------- Metodos de clase

    def guardar(self):
        productosList.append(self)


# --------------------- Herramientas globales -----------------------------------
productosList=[]

def listarProductos():
    for p in productosList:
        print("\n** {}  {}  {}  {}  {}  ".format(
            p.codigo,
            p.nombre,
            p.marca,
            p.precio,
            p.stock))

# ----------------------------------- test de clase ------------------------------

#Instanciamos:
pr1=Producto(1,"Arroz","DosHermano",100,10)
pr2=Producto(2,"Aceite 1lt","Alioli",50,10)
pr3=Producto(3,"leche","Serenisima",50,10)

listarProductos()
