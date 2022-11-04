from Proveedor import Proveedor,proveedorsList,Persona,editarProveedor



# Proveedor= nombre,telefono,direccion,cuit, razonSocial, categoria.

print("Test de tp...")
pr1=Proveedor(1,"salamandra SA","L")
pr2=Proveedor(2,"Unilever","C","0800")

for i in proveedorsList:
    print(i)
    print(" -----------")

editarProveedor(2,"Unilever SA","C","0800","BbAa")

for i in proveedorsList:
    print(i)
    print(" -----------")
 