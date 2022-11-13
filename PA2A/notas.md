
TP PROGRAMACION APLICADA / GRUPO 8

ENTREGA: 
    18 de Nov. / 10 a 30 minuts

INTEGRANTES: 
    FEDERICO A BRITEZ - MURILLO HORWELL
------------------------------------------------

DIAGRAMA DE CLASES SUGERIDO:

https://lucid.app/lucidchart/5b0938aa-6d37-4103-9d18-162bfae907e4/edit?viewport_loc=-2441%2C-1503%2C3207%2C1386%2C0_0&invitationId=inv_449d7960-d2d3-4527-a475-539baecccecd
------------------------------------------------

SE PIDE USAR LOS CONCEPTOS DE :

    -POO
    -clases
    -constructores
    -getters & setters SOLO los que se deban poder cambiar. (Ej: dniUsuario no)
    -metodos
    -App de consola o tkinter u otros para vista.

------------------------------------------------

MENU SUGERIDO

    pConsumo = [ arroz,fideos,azucar.aceite,leche]
    pLimpieza = [escoba,secador,trapo de piso,plumero, esponja]

CORRECIONES / ISSUS A REVISAR:
    Correcciones a realizar:
    -No toma telefono y direccion el cleinte creado
    -debe actualizar stock/precio la principal, no añadir a lista la segunda vez
    -editar cliente
    -editar proveedor
    -facturas

------------------------------------------------

PROGRAMA SUGERIDO PARA LA VISTA: Tkinter

https://docs.python.org/es/3/library/tkinter.html
------------------------------------------------

CONSIGNA:

    1. Dados los siguientes requisitos definir las clases y los atributos a desarrollar para llevar a
    cabo un sistema de Facturación de Minimercado PA2A
    El cliente PA2A necesita un sistema de Gestión de Negocios. PA2A es un minimercado el cual
    comercializa productos de consumo (bebidas y mercadería) y artículos de limpieza básicos. Trabaja
    con cuatro proveedores: Elizondo srl y Tito Srl para la compra de mercadería de consumo y
    SuperBrillo y Maxlimpito para los artículos de limpieza. Cada inicio de mes PA2A envía a sus
    proveedores un listado de mercadería a comprar para el mes y obtiene de sus proveedores los
    listados de precios respectivos. Realizada la compra de los productos se procede a la carga del
    sistema de los productos entrantes y actualización de stock. Así mismo se procede a la actualización
    de precios, se debe tener en cuenta que a los precios otorgados por los proveedores se les agrega un
    15% de incremento para registrar el precio de venta en el sistema.
    El Dueño de PA2A también requiere un registro de clientes a fin de poder obtener una cartera de
    clientes frecuentes a los cuales desea realizar descuentos especiales por asociarse al ClubPA2A, sin
    importar el medio de pago que el cliente use al momento de la compra. El descuento se aplica sobre
    el monto total de la compra.
    Con cada venta, el sistema debe realizar la actualización del stock correspondiente y generar y
    registrar la factura y/o ticket emitido con los descuentos efectuados (según el cliente sea o no socio)
    y el detalle de productos vendidos.
------------------------------------------------

.PY DE CLASE FACTURA Y CLASE FACTURADETALLE

    class Factura:
        def __init__(self,fecha,nrofactura,tipoFactura,detalle):
            self.fecha = fecha
            self._nrofactura=nrofactura
            self.tipoFactura=tipoFactura
    
    #Objeto Detalle de Factura

        @property
        def nrofactura(self, _nrofactura):
            return self._nrofactura

    class Detalle():
        def __init__(self,nroitem,producto,cantidad,precioUnitario):
            self._nroitem=nroitem
            self._producto=producto
            self._cantidad=cantidad
            self._precioUnitario=precioUnitario

------------------------------------------------