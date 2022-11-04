from Persona import Persona

class Cliente(Persona):
    def __init__(self, dni, nombre, esSocio=False, descuento=0,telefono="Null",direccion="Null") :
        super().__init__(telefono,direccion)
        self._dni=dni
        self._noombre=nombre
        self._esSocio=esSocio
        self._descuento=descuento
        self.guardar()
    
# ------------------------------ Metodos de clase

    def __str__(self):
        return "Dni: {} - Nombre: {} - Desc: {}%.  - Telefono: {} - Direccion: {}.".format(
            self.dni,
            self.nombre,
            self.descuento,
            self.telefono,
            self.direccion
        )
    
    def guardar(self):
        clienteNew=[self.dni,self.nombre,self.esSocio,self.descuento,self.telefono,self.direccion]
        clienteList.append(clienteNew)

# ---------------------------- Getters and Setters

    @property
    def dni(self):
        return self._dni
    
    @property
    def nombre(self):
        return self._noombre

    @property
    def esSocio(self):
        return self._esSocio
    
    @esSocio.setter
    def esSocio(self, estado):
        self._esSocio=estado
    
    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, nuevoDescuento):
        self._descuento=nuevoDescuento

# ------------------------------------------ Recursos de la clase

clienteList=[]

def editarCliente(dni, nombre, esSocio=False, descuento=0,telefono="Null",direccion="Null"):
        list=[dni, nombre, esSocio, descuento,telefono,direccion]
        for cliente in clienteList:
            if cliente[0]==list[0]:
                cliente[1]=list[1]
                cliente[2]=list[2]
                cliente[3]=list[3]
                cliente[4]=list[4]
                print("--cliente editado--\n")
