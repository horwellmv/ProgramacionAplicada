from Persona import Persona

class Cliente(Persona):
    def __init__(self, dni, nombre, descuento=0,telefono="Null",direccion="Null") :
        super().__init__(telefono,direccion)
        self._dni=dni
        self._nombre=nombre
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
        clienteList.append(self)
    
    def editar(self, descuento=0,telefono="Null",direccion="Null"):
            self.descuento=descuento
            self.telefono=telefono
            self.direccion=direccion
            print("-- Cliente editado! --\n")


    def afiliar(self, NewDescuento):
        self.descuento=NewDescuento
        print("-- Afiliacion exitosa! --\n")
    
# ---------------------------- Getters and Setters

    @property
    def dni(self):
        return self._dni
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, nuevoDescuento):
        self._descuento=nuevoDescuento

# ------------------------------------------ Recursos de la clase

clienteList=[]
