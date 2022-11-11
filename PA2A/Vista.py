import tkinter as tk

ventana1 = tk.Tk()
ventana1.geometry("700x500")



almacen=tk.Label(ventana1, text="ALMACEN PA2A", bg="green")
# Metodo Pack= 
# fill .X para estirar ancho.Y para estirar a lo largo, y .BOTH, expand = True para llenar la ventana
# side = tk.right o left o boton para ubicarla arriba abajo izq o der
#almacen.pack(fill=tk.X) 

#Grid de elementos, filas y columnas

boton1=tk.Button(ventana1, text="Boton 1")
boton2=tk.Button(ventana1, text="Boton 2")
boton3=tk.Button(ventana1, text="Boton 3")
boton4=tk.Button(ventana1, text="Boton 4")

boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)
boton3.grid(row=2,column=0)
boton4.grid(row=3,column=0)
'''
#Cajas de texto
clienteCaja=tk.Entry(ventana, font= "Helvetica 8")
clienteCaja.pack()

def TraerClienteTexto():
    text=clienteCaja.get()
    print(text)
    etiquetaDesdeTexto["text"]=text

#Botones
# Tamaño del boton padx=15,pady=30
# bt1=tk.Button(ventana,text=" texto del boton", command = miFuncion / ó / comman = Lambda: miFuncion(parametros))

clienteBotontexto= tk.Button(ventana,text="enviar de caja de texto", command=TraerClienteTexto)
clienteBotontexto.pack()

clienteBoton= tk.Button(ventana,text="Clientes", command=lambda: print("Nuevo cliente"))
clienteBoton.pack()

etiquetaDesdeTexto=tk.Label(ventana)
etiquetaDesdeTexto.pack()

'''
ventana1.mainloop()