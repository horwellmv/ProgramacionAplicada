from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, edad, fechaNacimiento, legajo, cargo, cantidadEmpleados, area):
        super().__init__(nombre, edad, fechaNacimiento, legajo, cargo)
        self._cantidadEmpleados=cantidadEmpleados
        self._area=area
    
    def __str__(self):
        return "Gerente: {}, Area: {},Cargo: {}, Empleados a cargo: {}.".format(
            self.nombre, self.area, self.cargo, self.cantidadEmpleados
        )
    
    @property
    def cantidadEmpleados(self):
        return self._cantidadEmpleados

    @cantidadEmpleados.setter
    def cantidadEmpleados(self,nuevaCantidad):
        self._cantidadEmpleados=nuevaCantidad
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self,nuevaArea):
        self._area=nuevaArea

    def asignarArea(self,nuevaArea):
        self.area=nuevaArea
    
