from Gerente import *
ger1 = Gerente("Valencia","30 años","31 Marzo 92", 123,"Product Manager",5,"Desarrollo")
'''
print(ger1)
ger1.asignarArea("Testing")
print(ger1)
ger1.cantidadEmpleados=10
print(ger1)'''

emple1= Empleado("Valencia",23,"Enero 2022",123,"Desarrollador")

print(emple1)
print(ger1)
emple1.modificarCargo("Administrativo")
ger1.modificarCargo("Ventas")
print(emple1)
print(ger1)