from Persona import Persona

class Proveedor(Persona):
    def __init__(self,cuit,razonSocial,categoria,telefono="Null",direccion="Null"):
        super().__init__(telefono,direccion)
        self._cuit=cuit
        self._razonSocial=razonSocial
        self._categoria=categoria
        self.guardar()
    

# ----------------------------- Metodos de la clase

    def __str__(self):
        return "Cuit: {} - Razon Social: {} - Categoria: {} - telefono: {} - Direccion: {}.".format(
            self.cuit,
            self.razonSocial,
            self.categoria,
            self.telefono,
            self.direccion
        )
    
    def guardar(self):
        proovedorNew=[self.cuit,self.razonSocial,self.categoria,self.telefono,self.direccion]
        proveedorsList.append(proovedorNew)

# ----------------------------- Getters & setters

    @property
    def cuit(self):
        return self._cuit

    @property
    def razonSocial(self):
        return self._razonSocial
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,nuevaCategoria):
        self._categoria=nuevaCategoria

# ----------------------------------------- Recursos de la clase

proveedorsList=[]

def editarProveedor(cuit,razonSocial,categoria,telefono="Null",direccion="Null"):
        list=[cuit,razonSocial,categoria,telefono,direccion]
        for proveedor in proveedorsList:
            if proveedor[0]==list[0]:
                proveedor[1]=list[1]
                proveedor[2]=list[2]
                proveedor[3]=list[3]
                proveedor[4]=list[4]
                print("--Proveedor editado--\n")
