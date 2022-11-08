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
        proveedorsList.append(self)
        print("-- Proveedor guardado! --\n")
    
    def editar(self,categoria,telefono="Null",direccion="Null"):
        self.categoria=categoria
        self.telefono=telefono
        self.direccion=direccion
        print("-- Proveedor editado! --\n")
    
    def remito(self):
        if self.categoria=="c":
            return pConsumo
        return pLimpieza

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

pConsumo = [["arroz",10,"PC001",450],["fideos",15,"PC002",200],["azucar",20,"PC3",150],["aceite",10,"PC004",350],["leche",50,"PC005",160]]
pLimpieza = [["escoba",5,"PL001",500],["secador",5,"PL002",300],["trapo de piso",5,"PL003",150],["plumero",5,"PL004",700],["esponja",5,"PL005",60]]

proveedorsList=[]

