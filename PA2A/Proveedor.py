from Persona import *
from ProductoConsumo import *
from ProductoLimpieza import *


# --------------------------------------- LISTAS PARA PERSISTENCIA
proveedorsList=[]

pConsumo = [
    ["arroz",10,"PC",450,"Ene/2023"],
    ["fideos",15,"PC",200,"Marz/2024"],
    ["azucar",20,"PC",150,"Feb/2023"],
    ["aceite",10,"PC",350,"Ago/2023"],
    ["leche",50,"PC",160,"Dic/2022"]
    ]

pLimpieza = [
    ["escoba",5,"PL",500,"lote11"],
    ["secador",5,"PL",300,"lote22"],
    ["trapo_de_piso",5,"PL",150,"lote33"],
    ["plumero",5,"PL",700,"lote44"],
    ["esponja",5,"PL",60,"lote55"]
    ]


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
        print("-- {} guardado! --\n".format(self.razonSocial))
    
    def editar(self,telefono="Null",direccion="Null"):
        self.telefono=telefono
        self.direccion=direccion
        print("-- {} editado! --\n".format(self.razonSocial))
    
    def remito(self):
        #["arroz",10,"PC",450,"Ene/2023"]
        if self.categoria=="PC":
            for pC in pConsumo:
                pC[0]=ProductoConsumo(pC[0],pC[1],pC[2],pC[3],pC[4])
            print("\n-- Remito pConsumo creado exitosamente --\n")
        
        if self.categoria=="PL":
            for pL in pLimpieza:
                pL[0]=ProductoLimpieza(pL[0],pL[1],pL[2],pL[3],pL[4])
            print("\n-- Remito pLimpieza creado exitosamente --\n")
        return productosList

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

