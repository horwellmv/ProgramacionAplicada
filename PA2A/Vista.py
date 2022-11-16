from tkinter import *
from tkinter import ttk

# -------------------------
from Cliente import *
from Proveedor import *
from DetalleFactura import *
from Factura import *


def limpiar(tabla):
    limpiar=tabla.get_children()
    for i in limpiar:
        tabla.delete(i)
        

# Consumo= producto, stock: int, categoria, precio: int, vencimiento
# Limpieza= producto, stock: int, categoria, precio: int, lote

#VENTANA PRINCIPAL.
root = Tk()
root.title('SUPERMERCADO PA2A')
root.geometry("870x400")

#INCLUIMOS PANEL PARA LAS PESTAÑAS.
nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

#CREAMOS PESTAÑAS
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)

# ------------------------------------------------------------------------------------------------------ P R I N C I P A L
# VARIABLES PARA INSTANCIAR PRINCIPAL

# Consumo= producto, stock: int, categoria, precio: int, vencimiento
# Limpieza= producto, stock: int, categoria, precio: int, lote

def generarRemito():
    prov=NombreProv.get()
    for i in proveedorsList:
        if i.razonSocial==prov:
            i.remito()
            print("productos fabricados")
    print("Se ejcuto metodo remito")


def traerProductos():
    limpiar(treePr)
    for i in productosList:
        if i.categoria=="PC":
            treePr.insert('', 'end', text=i.producto, values=(i.stock,i.categoria,i.precio,i.vencimiento))
        if i.categoria=="PL":
            treePr.insert('', 'end', text=i.producto, values=(i.stock,i.categoria,i.precio,i.lote))



NombreProv = StringVar()

#ELEMENTOS PESTAÑA PRINCIPAL
cuitL=Label(p1,text="PROVEEDOR:").grid(row=0,column=0,)
cuitE=Entry(p1, textvariable=NombreProv).grid(row=0,column=1)


# Botones Principal
bt1=Button(p1, text='NUEVO REMITO',bg='light blue',command=generarRemito).grid(row=2,column=1)
bt2=Button(p1, text='REFRESCAR',bg='light blue',command=traerProductos).grid(row=10,column=1)


# Tabla Principal
treePr=ttk.Treeview(p1,columns=("stock","categoria","precio","detalle"))
treePr.column("#0",width=190)
treePr.column("stock",width=70,anchor=CENTER)
treePr.column("categoria",width=90,anchor=CENTER)
treePr.column("precio",width=90,anchor=CENTER)
treePr.column("detalle",width=140,anchor=CENTER)

treePr.heading("#0",text="PRODUCTO")
treePr.heading("stock",text="STOCK")
treePr.heading("categoria",text="CATEGORIA")
treePr.heading("precio",text="PRECIO")
treePr.heading("detalle",text="DETALLE")

treePr.grid(row=4,column=7)

# ---------------------------------------------------------------------------------------------------------------- V E N T A S

cli1=Cliente(1,"Horwell",10)
cli2=Cliente(2,"Gigi",5)


pr1=ProductoConsumo("coca",10,"PC",100,"marzo")
pr2=ProductoConsumo("coco",10,"PC",200,"marzo")
pr3=ProductoConsumo("cacao",10,"PC",500,"marzo")
pr4=ProductoLimpieza("trapo",10,"PL",10,"lote1")


def detalleVenta():
    for i in productosList:
        if i.producto==articulo.get():
            newDetalle(i.producto,cantidad.get())
            print("TK: Metodo NewDetalle ejecutado")
    traerDetalles()

def newFactura():
    if len(DetalleList)==0:
        print("TK: Metodo newfactura: No hay detalles a facturar")
    else:
        x=Factura(ticket.get(),dniConsumidor.get())
        total.set(x)
        print("TK: MEtodo newFactura: Realizado con exito")
        print(x)
        newTicket=int(ticket.get())
        newTicket=newTicket+1
        ticket.set(newTicket)

def traerDetalles(): #self.articulo,.cantidad, .precioU,.total
    limpiar(treeV)
    for i in DetalleList:
        treeV.insert('', 'end', text=i.cantidad, values=(i.articulo,i.precioU,i.total))

#ELEMENTOS PESTAÑA VENTAS
ticket =IntVar()
ticket.set(900000001)
dniConsumidor = IntVar()
articulo = StringVar()
cantidad= IntVar()
total= StringVar()


TicketL=Label(p2,text="Ticket N°:").grid(row=0,column=0, pady=15)
TicketV=Label(p2, textvariable=ticket).grid(row=0,column=1, pady=15)

telefonoL=Label(p2,text="Cliente DNI:").grid(row=0,column=5)
telefonoE=Entry(p2, textvariable=dniConsumidor).grid(row=0,column=6)

ArticuloV=Label(p2,text="Articulo:").grid(row=1,column=0)
ArticuloE=Entry(p2, textvariable=articulo).grid(row=1,column=1)

descuentoL=Label(p2,text="Cantidad:").grid(row=1,column=5)
descuentoE=Entry(p2, textvariable=cantidad).grid(row=1,column=6)

TotalL=Label(p2,text="TOTAL: $ ").grid(row=7,column=6)
TotalL2=Label(p2, textvariable=total).grid(row=7,column=7)

# BOTONES VENTAS
bt1=Button(p2, text='AGREGAR',bg='light blue',command=detalleVenta).grid(row=2,column=6)
bt2=Button(p2, text='FACTURAR',bg='light blue',command=newFactura).grid(row=10,column=6)

# TABLA VENTAS
treeV=ttk.Treeview(p2,columns=("producto","precioU","precioT"))
treeV.column("#0",width=70)
treeV.column("producto",width=180,anchor=CENTER)
treeV.column("precioU",width=100,anchor=CENTER)
treeV.column("precioT",width=100,anchor=CENTER)

treeV.heading("#0",text="UNIDADES")
treeV.heading("producto",text="PRODUCTO")
treeV.heading("precioU",text="$ PRECIO Un")
treeV.heading("precioT",text="$ PRECIO Tot")

treeV.grid(row=4,column=7)


# ---------------------------------------------------------------------------------------------------------------- C L I E N T E S
def newCliente():
    Cliente(dni.get(),nombre.get(),descuento.get(),telefono.get(),direccion.get())
    print("TK: creado Cliente ",nombre.get())
    for i in clienteList:
        print(i)

def traerClientes():
    limpiar(treeC)
    for i in clienteList:
        treeC.insert('', 'end', text=i.dni, values=(i.nombre,i.descuento,i.telefono,i.direccion))

# VARIABLES PARA INSTANCIAR CLIENTE
#dni:int, nombre, descuento:int=0,telefono="Null",direccion="Null"

dni = IntVar()
nombre = StringVar()
descuento = IntVar()
telefono = StringVar()
direccion = StringVar()

#ELEMENTOS PESTAÑA CLIENTES

dniL=Label(p3,text="Dni:").grid(row=0,column=0)
dniE=Entry(p3, textvariable=dni).grid(row=0,column=1)

nombreL=Label(p3,text="Nombre:").grid(row=1,column=0)
nombreE=Entry(p3, textvariable=nombre).grid(row=1,column=1)

descuentoL=Label(p3,text="Descuento:").grid(row=2,column=0)
descuentoE=Entry(p3, textvariable=descuento).grid(row=2,column=1)

telefonoL=Label(p3,text="Telefono:").grid(row=0,column=5)
telefonoE=Entry(p3, textvariable=telefono).grid(row=0,column=6)

direccionL=Label(p3,text="Direccion:").grid(row=1,column=5)
direccionE=Entry(p3, textvariable=direccion).grid(row=1,column=6)

# Botones Cliente
bt1=Button(p3, text='AGREGAR',bg='light blue',command=newCliente).grid(row=2,column=6)
bt2=Button(p3, text='REFRESCAR',bg='light blue',command=traerClientes).grid(row=10,column=6)

# Tabla clientes
treeC=ttk.Treeview(p3,columns=("nombre","descuento","telefono","direccion"))
treeC.column("#0",width=50)
treeC.column("nombre",width=150,anchor=CENTER)
treeC.column("descuento",width=80,anchor=CENTER)
treeC.column("telefono",width=80,anchor=CENTER)
treeC.column("direccion",width=120,anchor=CENTER)

treeC.heading("#0",text="DNI")
treeC.heading("nombre",text="NOMBRE")
treeC.heading("descuento",text="% DESC")
treeC.heading("telefono",text="TELEFONO")
treeC.heading("direccion",text="DIRECCION")

treeC.grid(row=4,column=7)

# --------------------------------------------------------------------------------------------------------- P R O V E E D O R E S

#cuit,razonSocial,categoria,telefono="Null",direccion="Null"
def newProveedor():
    p=Proveedor(cuit.get(),rSocial.get(),categoria.get(),telefonoP.get(),direccionP.get())
    print("TK: Creado Proveedor ",rSocial.get())

def traerProveedores():
    limpiar(treeP)
    for i in proveedorsList:
        treeP.insert('', 'end', text=i.cuit, values=(i.razonSocial,i.categoria,i.telefono,i.direccion))


# VARIABLES PARA INSTANCIAR PROVEEDOR
#cuit,razonSocial,categoria,telefono="Null",direccion="Null"
cuit = IntVar()
rSocial = StringVar()
categoria = StringVar()
telefonoP = StringVar()
direccionP = StringVar()

# ELEMENTOS PESTAÑA PROVEEDORES
#cuit,razonSocial,categoria,telefono="Null",direccion="Null"


cuitL=Label(p4,text="Cuit:").grid(row=0,column=0)
cuitE=Entry(p4, textvariable=cuit).grid(row=0,column=1)

razSocialL=Label(p4,text="R.Social:").grid(row=1,column=0)
razSocialE=Entry(p4, textvariable=rSocial).grid(row=1,column=1)

categoriaL=Label(p4,text="Categoria:").grid(row=2,column=0)
categoriaE=Entry(p4, textvariable=categoria).grid(row=2,column=1)

telefonoL=Label(p4,text="Telefono:").grid(row=0,column=5)
telefonoE=Entry(p4, textvariable=telefonoP).grid(row=0,column=6)

direccionL=Label(p4,text="Direccion:").grid(row=1,column=5)
direccionE=Entry(p4, textvariable=direccionP).grid(row=1,column=6)

# Botones Proveedores
bt1=Button(p4, text='AGREGAR',bg='light blue',command=newProveedor).grid(row=2,column=6)
bt2=Button(p4, text='REFRESCAR',bg='light blue',command=traerProveedores).grid(row=10,column=6)


# Tabla proveedores
treeP=ttk.Treeview(p4,columns=("rSocial","categoria","telefono","direccion"))
treeP.column("#0",width=50)
treeP.column("rSocial",width=150,anchor=CENTER)
treeP.column("categoria",width=80,anchor=CENTER)
treeP.column("telefono",width=80,anchor=CENTER)
treeP.column("direccion",width=120,anchor=CENTER)

treeP.heading("#0",text="CUIT")
treeP.heading("rSocial",text="R. SOCIAL")
treeP.heading("categoria",text="CATEGORIA")
treeP.heading("telefono",text="TELEFONO")
treeP.heading("direccion",text="DIRECCION")

treeP.grid(row=4,column=7)


# --------------------------------------------------------------------------------- A G R E G A M O S   P E S T A Ñ A S    C R E A D A S 
nb.add(p1,text='PRINCIPAL')
nb.add(p2,text='VENTAS')
nb.add(p3,text='CLIENTES')
nb.add(p4,text='PROVEEDORES')

root.mainloop()

'''
#APUNTES..

#Cajas de texto
Caja=tk.Entry(ventana, font= "Helvetica 8")

def TraerClienteTexto():
    text=clienteCaja.get()
    print(text)
    etiquetaDesdeTexto["text"]=text

#Botones
# Tamaño del boton padx=15,pady=30
# bt1=tk.Button(ventana,text=" texto del boton", command = miFuncion / ó / comman = Lambda: miFuncion(parametros))

clienteBotontexto= tk.Button(ventana,text="enviar de caja de texto", command=TraerClienteTexto)
clienteBotontexto.pack()

etiquetaDesdeTexto=tk.Label(ventana)
etiquetaDesdeTexto.pack()
'''